import numpy as np
# import mysql.connector
import asyncio
import json
from threading import Thread
import time
from typing import Dict, Any
from urllib.parse import urlparse
from flask import Blueprint, Flask, request
from server.constant.constants import MAX_ISOLATED_URL_BATCH_LENGTH, FROM_ISOLATED_URL, ADD_ISOLATED_URL_CONTENT, DELETE_ISOLATED_URL_CONTENT
from server.app.utils.decorators import token_required
from server.app.utils.sqlite_client import get_db_connection
from server.app.utils.diskcache_lock import diskcache_lock
from server.app.utils.url_helper import is_valid_url, normalize_url
from server.logger.logger_config import my_logger as logger
from server.rag.index.parser.html_parser.web_content_crawler import AsyncCrawlerSiteContent

from prompt import TASK_PROMPTS
from zhipuai import ZhipuAI
import re


urls_bp = Blueprint('urls', __name__, url_prefix='/open_kf_api/urls')


def async_isolated_url_content_task(url_dict: Dict[int, str], task_type: int) -> None:
    """
    Starts the asynchronous crawl and embedding process for a list of isolated urls.

    task_type:
      1 - add_content
      2 - delete_content
    """

    """Start the crawl content task in an asyncio event loop."""
    logger.info(
        f"async_isolated_url_content_task begin! url_dict: {url_dict}, task_type: {task_type}")
    crawler_content = AsyncCrawlerSiteContent(
        domain_list=[],
        doc_source=FROM_ISOLATED_URL
    )

    # Run the crawler
    if task_type == ADD_ISOLATED_URL_CONTENT:
        asyncio.run(crawler_content.add_content(url_dict))
    elif task_type == DELETE_ISOLATED_URL_CONTENT:
        asyncio.run(crawler_content.delete_content(url_dict))
    logger.info(f"async_isolated_url_content_task end!")


@urls_bp.route('/submit_isolated_url_list', methods=['POST'])
@token_required
def submit_isolated_url_list() -> Dict[str, Any]:
    data = request.json
    url_list = data.get('url_list')

    if not url_list:
        return {'retcode': -20000, 'message': 'url_list is required', 'data': {}}

    if len(url_list) > MAX_ISOLATED_URL_BATCH_LENGTH:
        return {'retcode': -20001, 'message': f"The size of 'url_list' is {len(url_list)}, which is greater than {MAX_ISOLATED_URL_BATCH_LENGTH}", 'data': {}}

    normalized_url_list = []
    for url in url_list:
        if not is_valid_url(url):
            logger.error(f"url: '{url}' is not a valid URL!")
            return {'retcode': -20002, 'message': f"url: '{url}' is not a valid URL", 'data': {}}
        normalized_url_list.append(normalize_url(url))

    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # Find which URLs already exist in the database
        placeholders = ', '.join(['?'] * len(normalized_url_list))
        cur.execute(
            f"SELECT id, url FROM t_isolated_url_tab WHERE url IN ({placeholders})", normalized_url_list)
        existing_urls = {row['url']: row['id'] for row in cur.fetchall()}
        logger.warning(f"The existing_urls is {existing_urls}")

        # Determine new and existing URLs
        existing_to_update = []
        new_to_insert = []

        timestamp = int(time.time())
        for url in normalized_url_list:
            if url in existing_urls:
                existing_to_update.append((timestamp, existing_urls[url]))
            else:
                new_to_insert.append((url, timestamp, timestamp))

        try:
            with diskcache_lock.lock():
                # Update all existing URLs in one operation
                if existing_to_update:
                    cur.executemany(
                        "UPDATE t_isolated_url_tab SET doc_status = 1, mtime = ? WHERE id = ?", existing_to_update)

                # Insert all new URLs in one operation
                if new_to_insert:
                    cur.executemany(
                        "INSERT INTO t_isolated_url_tab (url, content, content_length, content_md5, doc_status, ctime, mtime) VALUES (?, '[]', 0, '', 1, ?, ?)", new_to_insert)

                conn.commit()
        except Exception as e:
            logger.error(f"Process discache_lock exception: {e}")
            return {'retcode': -30000, 'message': f'An error occurred: {e}', 'data': {}}

        cur.execute(
            f"SELECT id, url FROM t_isolated_url_tab WHERE url IN ({placeholders})", normalized_url_list)
        url_dict = {row['id']: row['url'] for row in cur.fetchall()}

        # Start the asynchronous crawl task
        Thread(target=async_isolated_url_content_task, args=(
            url_dict, ADD_ISOLATED_URL_CONTENT)).start()

        return {'retcode': 0, 'message': 'URLs processed successfully', 'data': {'url_id_list': list(url_dict.keys())}}
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return {'retcode': -30000, 'message': f'An error occurred: {e}', 'data': {}}
    finally:
        if conn:
            conn.close()


@urls_bp.route('/get_isolated_url_list', methods=['POST'])
@token_required
def get_isolated_url_list():
    data = request.json
    url_id_list = data.get('id_list', None)  # Make site an optional parameter

    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        if url_id_list:
            placeholders = ', '.join(['?'] * len(url_id_list))
            cur.execute(
                f"SELECT id, url, content_length, doc_status, ctime, mtime FROM t_isolated_url_tab WHERE id IN ({placeholders})", url_id_list)
        else:
            cur.execute(
                "SELECT id, url, content_length, doc_status, ctime, mtime FROM t_isolated_url_tab")

        rows = cur.fetchall()
        response_data = {}
        response_data['url_list'] = [dict(row) for row in rows]
        return {'retcode': 0, 'message': 'Success', 'data': response_data}
    except Exception as e:
        logger.error(f"An error occurred while fetching URL list: {e}")
        return {'retcode': -30000, 'message': f'An error occurred: {e}', 'data': {}}
    finally:
        if conn:
            conn.close()


@urls_bp.route('/delete_isolated_url_list', methods=['POST'])
@token_required
def delete_isolated_url_list():
    data = request.json
    url_id_list = data.get('id_list')

    if not url_id_list:
        return {'retcode': -20000, 'message': 'id_list is required', 'data': {}}

    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        placeholders = ', '.join(['?'] * len(url_id_list))
        cur.execute(
            f"SELECT id, url FROM t_isolated_url_tab WHERE id IN ({placeholders})", url_id_list)
        url_dict = {row['id']: row['url'] for row in cur.fetchall()}

        # Use threading to avoid blocking the Flask application
        Thread(target=async_isolated_url_content_task, args=(
            url_dict, DELETE_ISOLATED_URL_CONTENT)).start()

        return {'retcode': 0, 'message': 'Started deleting the isolated URL list embeddings.', 'data': {}}
    except Exception as e:
        logger.error(f"An error occurred while fetching URL list: {e}")
        return {'retcode': -30000, 'message': f'An error occurred: {e}', 'data': {}}
    finally:
        if conn:
            conn.close()


@urls_bp.route('/get_isolated_url_sub_content_list', methods=['POST'])
@token_required
def get_isolated_url_sub_content_list():
    data = request.json
    url_id = data.get('id')
    page = data.get('page')
    page_size = data.get('page_size')

    # Validate mandatory parameters
    if None in (url_id, page, page_size):
        return {'retcode': -20000, 'message': 'Missing mandatory parameters', 'data': {}}

    if not isinstance(page, int) or not isinstance(page_size, int) or page < 1 or page_size < 1:
        return {'retcode': -20001, 'message': 'Invalid page or page_size parameters', 'data': {}}

    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # Retrieve the content from the database
        cur.execute(
            'SELECT content FROM t_isolated_url_tab WHERE id = ?', (url_id,))
        row = cur.fetchone()
        if not row:
            return {'retcode': -30000, 'message': 'Content not found', 'data': {}}

        content = row['content']
        content_vec = json.loads(content)

        # Calculate pagination details
        total_count = len(content_vec)
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        if start_index > 0 and start_index >= total_count:
            return {'retcode': -20002, 'message': 'Page number out of range', 'data': {}}

        # Slice the content vector to get the sub-content list for the current page
        sub_content_list = [
            {"index": start_index + index + 1,
                "content": part, "content_length": len(part)}
            for index, part in enumerate(content_vec[start_index:end_index], start=start_index)
        ]

        return {
            "retcode": 0,
            "message": "success",
            "data": {
                "total_count": total_count,
                "sub_content_list": sub_content_list
            }
        }
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return {'retcode': -30001, 'message': 'Database exception', 'data': {}}
    finally:
        if conn:
            conn.close()


@urls_bp.route('/get_code_score', methods=['POST'])
def score():
    data = request.get_json()
    print("进入请求，获取请求数据")
    print(data)
    stu_code = data['code']
    problem = data['question']
    # 题目id
    if stu_code is None:
        print("代码为空，不存在！")
        return {
            'code': 0,
            'msg': '代码不存在',
            'data': {}
        }
    else:
        # glm-4评分
        print("进行评分！！")
        # print(stu_code)
        score_results = evaluate(problem=problem, output=stu_code)
        score_json = extract_json_with_regex(score_results)
        print("score json:", score_json)
        score = json.loads(score_json)
        suggestion = suggest(
            problem=problem, output=stu_code, score=score_results)
        # e_dict = {
        #     'usefulness':score['usefulness'],
        #     'functional correctness':score['functional correctness'],
        #     'coding style':score['coding style'],
        #     'suggestion':suggestion }

        return {
            'code': 1,
            'msg': "成功！",
            'data': {
                'usefulness': score['usefulness'],
                'functional correctness': score['functional correctness'],
                'coding style': score['coding style'],
                'suggestion': suggestion
            }
        }

    # 存给数据库


# 调用glm-4评分

def evaluate(problem, output, reference=None, task="code-gen", aspect="usefulness"):

    prompts = TASK_PROMPTS[task][aspect]["reference-enhanced"]
    prompts = prompts.replace(
        "{{PROBLEM}}", problem).replace("{{OUTPUT}}", output)
    # 请填写您自己的APIKey
    client = ZhipuAI(
        api_key="b0ad56a7d242ea250dc91314011c6d62.93hSt0HhQyIZOCwR")
    response = client.chat.completions.create(
        model="glm-4",
        messages=[
            {"role": "user", "content": prompts},
        ],
    )

    raw_output = response.choices[0].message.content
    print(raw_output)
    return raw_output


def suggest(problem, output, score, task='code-gen', aspect='suggestion'):
    prompts = TASK_PROMPTS[task][aspect]["reference-enhanced"]
    prompts = prompts.replace("{{PROBLEM}}", problem).replace(
        "{{OUTPUT}}", output).replace("{{SCORE}}", score)

    # 请填写您自己的APIKey
    client = ZhipuAI(
        api_key="b0ad56a7d242ea250dc91314011c6d62.93hSt0HhQyIZOCwR")
    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=[
            {"role": "user", "content": prompts},
        ],
    )

    raw_output = response.choices[0].message.content
    print(raw_output)
    return raw_output


# def extract_json_with_regex(text):
#     pattern = r'```json\s*(.*?)\s*```'
#     match = re.search(pattern, text, re.DOTALL)
#     if match:
#         return match.group(1)
#     else:
#         return text


# def extract_json_with_regex(text):
#     pattern = r'\{(.*?)\}'
#     match = re.search(pattern, text, re.DOTALL)
#     if match:
#         return match.group(1)
#     else:
#         return None


def extract_json_with_regex(text):
    # 查找第一个花括号之间的内容
    start_index = text.find('{')
    end_index = text.find('}')
    json_str = text[start_index:end_index + 1]

    try:
        # 尝试解析为JSON
        json_data = json.loads(json_str)
        # 转换为去除多余字符和换行符的JSON格式字符串
        cleaned_json_str = json.dumps(json_data, separators=(',', ':'))
        return cleaned_json_str
    except json.JSONDecodeError:
        # 如果解析失败，返回空字符串或其他适当的处理方式
        return ''

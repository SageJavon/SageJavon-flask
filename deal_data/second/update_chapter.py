import mysql.connector
from mysql.connector import Error

# MySQL数据库连接配置
db_config = {
    'host': 'mysql.mysql',
    'database': 'sage_javon',
    'user': 'root',
    'password': 'pYRGObpCdG',
    'port': '3306'  # 默认MySQL端口
}

# chapter_mapping 示例
chapter_mapping = {
    1: {"chapter": "Java概述", "knowledge_points": ["Java字符编码", "文件扩展名"]},
    2: {"chapter": "Java环境搭建和程序初体验", "knowledge_points": ["编译运行", "主方法"]},
    # ... 其他章节映射
}

def get_chapter_for_knowledge(knowledge_point):
    for chapter_id, data in chapter_mapping.items():
        if knowledge_point in data['knowledge_points']:
            return chapter_id
    return None

def update_exercise_chapters():
    try:
        # 连接MySQL数据库
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # 获取所有 exercise 的 id
        cursor.execute("SELECT id FROM exercise")
        exercises = cursor.fetchall()

        for exercise in exercises:
            exercise_id = exercise[0]

            # 查找对应的 knowledge_ids
            cursor.execute("SELECT knowledge_id FROM exercise_knowledge WHERE exercise_id = %s", (exercise_id,))
            knowledge_ids = cursor.fetchall()

            knowledge_points = []
            for k_id in knowledge_ids:
                cursor.execute("SELECT knowledge_point FROM knowledge WHERE id = %s", (k_id[0],))
                knowledge_point = cursor.fetchone()
                if knowledge_point:
                    knowledge_points.append(knowledge_point[0])

            # 查找章节
            chapters = set()
            for point in knowledge_points:
                chapter_id = get_chapter_for_knowledge(point)
                if chapter_id is not None:
                    chapters.add(chapter_id)

            # 更新章节（假设每道题目对应一个章节，这里取第一个章节作为示例）
            if chapters:
                new_chapter = list(chapters)[0]
                cursor.execute("UPDATE exercise SET chapter = %s WHERE id = %s", (new_chapter, exercise_id))
                print(f"更新 exercise_id={exercise_id} 的章节为 {new_chapter}")

        # 提交事务
        conn.commit()
        print("所有章节更新成功")

    except Error as e:
        print(f"数据库操作错误: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("数据库连接已关闭")

# 执行更新操作
update_exercise_chapters()

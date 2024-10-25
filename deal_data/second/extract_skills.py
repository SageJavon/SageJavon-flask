import pandas as pd
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

# TXT文件路径
txt_file = './knowledge_names.txt'

def export_knowledge_names_to_txt(db_config, txt_file):
    print("开始执行数据库操作...")  # 1. 确认函数执行了
    try:
        # 连接MySQL数据库
        print("尝试连接数据库...")  # 2. 确认到达了数据库连接
        conn = mysql.connector.connect(**db_config, buffered=True)
        print("数据库连接成功！")  # 3. 数据库连接成功后
        
        cursor = conn.cursor()

        # 查询knowledge表中的name字段
        print("查询知识表中的name字段...")
        cursor.execute("SELECT name FROM knowledge")
        knowledge_names = cursor.fetchall()
        
        print(f"查询到的知识名称数量: {len(knowledge_names)}")  # 4. 打印查询到的结果数量

        # 检查是否有结果
        if not knowledge_names:
            print("没有找到任何知识名称")
            return

        # 将结果写入TXT文件
        with open(txt_file, 'w', encoding='utf-8') as f:
            for name in knowledge_names:
                f.write(f"{name[0]}\n")

        print("知识名称已成功导出到TXT文件")

    except Error as e:
        print(f"数据库操作错误: {e}")
    except Exception as e:
        print(f"其他错误: {e}")

    finally:
        # 关闭数据库连接
        if conn is not None and conn.is_connected():
            cursor.close()
            conn.close()
            print("数据库连接已关闭")

# 执行导出操作
export_knowledge_names_to_txt(db_config, txt_file)

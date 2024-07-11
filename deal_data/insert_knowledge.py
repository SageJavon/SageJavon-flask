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

# txt文件路径和文件名
txt_file = './skill_names.txt'

# MySQL表名
mysql_table = 'knowledge'


def insert_knowledge_to_mysql(txt_file, mysql_table, db_config):
    try:
        # 连接MySQL数据库
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # 读取txt文件内容
        with open(txt_file, 'r', encoding='utf-8') as file:
            knowledge_list = file.readlines()

        if not knowledge_list:
            print("txt文件为空")
            return

        # 插入剩余记录，parent_id为第一条记录的id
        sql_insert_others = f"INSERT INTO {mysql_table} (parent_id, name, knowledge, num_q) VALUES (%s, %s, %s, %s)"
        for i, knowledge in enumerate(knowledge_list[1:], start=1):
            cursor.execute(sql_insert_others,
                           (1, knowledge.strip(), knowledge.strip(), i + 1))

        # 提交到数据库执行
        conn.commit()
        print("数据插入成功")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # 关闭数据库连接
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("数据库连接已关闭")


# 执行插入操作
insert_knowledge_to_mysql(txt_file, mysql_table, db_config)

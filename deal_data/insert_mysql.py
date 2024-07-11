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

# CSV文件路径和文件名
csv_file = './choice_questionssss.csv'

# MySQL表名
mysql_table = 'knowledge'


def insert_data_to_mysql(csv_file, mysql_table, db_config):
    try:
        # 连接MySQL数据库
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # 读取CSV文件到DataFrame
        df = pd.read_csv(csv_file, encoding='utf-8')

        # 迭代处理每一行数据
        for row in df.itertuples(index=False):
            print(row[1])
            # 准备插入语句
            sql = f"INSERT INTO {mysql_table} (question_text, correct_answer, difficulty, choice_a, choice_b, choice_c, choice_d, type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (row[1], row[7], row[8], row[3],
                      row[4], row[5], row[6], 0)

            # 执行插入操作
            cursor.execute(sql, values)

        # 提交到数据库执行
        conn.commit()
        print("数据插入成功")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # 关闭数据库连接
        if conn is not None and conn.is_connected():
            cursor.close()
            conn.close()
            print("数据库连接已关闭")


# 执行插入操作
insert_data_to_mysql(csv_file, mysql_table, db_config)

import pandas as pd
import mysql.connector
from mysql.connector import Error, errorcode

# MySQL数据库连接配置
db_config = {
    'host': 'mysql.mysql',
    'database': 'sage_javon',
    'user': 'root',
    'password': 'pYRGObpCdG',
    'port': '3306'  # 默认MySQL端口
}

# CSV 文件路径
csv_file = '../second/choice-second.csv'

def insert_csv_to_mysql(csv_file, db_config):
    try:
        # 连接MySQL数据库
        print(csv_file)
        print(db_config)
        conn = mysql.connector.connect(**db_config)
        print(conn.get_server_version())
        print('Connected to MySQL database')
        cursor = conn.cursor()

        # 读取CSV文件到DataFrame
        df = pd.read_csv(csv_file)

        # 遍历每一行并插入数据库
        for index, row in df.iterrows():
            sql_insert = """
            INSERT INTO exercise (question_text, correct_answer, difficulty, choice_a, choice_b, choice_d,type,chapter,choice_c)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)
            """
            values = (
                row['problem_text'],
                row['answer'],
                row['level'],
                row['choiceA'],
                row['choiceB'],
                row['choiceD'] ,
                1,
                "java初体验",
                row['choiceC']
            )
            cursor.execute(sql_insert, values)

        # 提交事务
        conn.commit()
        print("CSV 数据成功插入数据库")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("用户名或密码错误")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("数据库不存在")
        else:
            print(err)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("数据库连接已关闭")

# 执行插入操作
insert_csv_to_mysql(csv_file, db_config)

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
exercise_table = 'exercise'
knowledge_table = 'knowledge'
relationship_table = 'exercise_knowledge'


def insert_relationship_to_mysql(csv_file, db_config):
    try:
        # 连接MySQL数据库
        conn = mysql.connector.connect(**db_config, buffered=True)
        cursor = conn.cursor()

        # 读取CSV文件到DataFrame
        df = pd.read_csv(csv_file)

        # 迭代处理每一行数据
        for index, row in df.iterrows():
            question_text = row['problem_text']
            skill_names = str(row['skill_name']).split(',')

            # 获取exercise_id
            cursor.execute(
                f"SELECT id FROM {exercise_table} WHERE question_text = %s", (question_text,))
            exercise_id = cursor.fetchone()
            if exercise_id is not None:
                exercise_id = exercise_id[0]
            else:
                print(f"没有找到question_text为'{question_text}'的记录")
                continue

            # 获取每个skill_name的knowledge_id并插入关系表
            for skill_name in skill_names:
                skill_name = skill_name.strip()
                cursor.execute(
                    f"SELECT id FROM {knowledge_table} WHERE name = %s", (skill_name,))
                knowledge_id = cursor.fetchone()
                if knowledge_id is not None:
                    knowledge_id = knowledge_id[0]
                else:
                    print(f"没有找到skill_name为'{skill_name}'的记录")
                    continue

                # 插入到关系表
                sql_insert_relationship = f"INSERT INTO {relationship_table} (knowledge_id, exercise_id) VALUES (%s, %s)"
                cursor.execute(sql_insert_relationship,
                               (knowledge_id, exercise_id))

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
insert_relationship_to_mysql(csv_file, db_config)

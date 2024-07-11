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
csv_file = './program_records.csv'

# MySQL表名
exercise_table = 'exercise'
knowledge_table = 'knowledge'
relationship_table = 'exercise_knowledge'


def get_skill_names(knowledge_ids, cursor):
    # 根据knowledge_ids查询knowledge表获取对应的knowledge名称
    skill_names = []
    for knowledge_id in knowledge_ids:
        query = f"""
                SELECT name
                FROM {knowledge_table}
                WHERE id = {knowledge_id}
                """
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            skill_names.append(result[0])
    return '_'.join(skill_names)


def insert_relationship_to_csv(csv_file, db_config):
    try:
        # 连接MySQL数据库
        conn = mysql.connector.connect(**db_config, buffered=True)
        cursor = conn.cursor()

        # 读取CSV文件到DataFrame
        df = pd.read_csv(csv_file)

        # 初始化数据库中的起始problem_id
        start_problem_id = 112

        # 迭代处理每一行数据
        for index, row in df.iterrows():
            exercise_id = row['database_problem_id']

            # 查询relationship_table，找到对应exercise_id的所有knowledge_id
            query = f"""
                    SELECT knowledge_id
                    FROM {relationship_table}
                    WHERE exercise_id = {exercise_id}
                    """

            cursor.execute(query)
            results = cursor.fetchall()

            if results:
                # 获取所有knowledge_id
                knowledge_ids = [result[0] for result in results]
                # 根据knowledge_ids查询对应的knowledge名称，并连接成字符串
                skill_names = get_skill_names(knowledge_ids, cursor)
                # 将获取到的skill_ids和skill_names写入到DataFrame的相应列中
                df.at[index, 'skill_id'] = '_'.join(map(str, knowledge_ids))
                df.at[index, 'skill_name'] = skill_names

        # 将修改后的DataFrame保存回CSV文件
        output_csv_file = './output.csv'
        df.to_csv(output_csv_file, index=False)

        print(f"CSV文件处理完成，并保存为 {output_csv_file}")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()


# 调用函数处理CSV文件和数据库关系
insert_relationship_to_csv(csv_file, db_config)

import mysql.connector
import pandas as pd

# MySQL数据库连接配置
db_config = {
    'host': 'mysql.mysql',
    'database': 'sage_javon',
    'user': 'root',
    'password': 'pYRGObpCdG',
    'port': '3306'  # 默认MySQL端口
}

def count_exercises_by_chapter(db_config):
    try:
        # 连接MySQL数据库
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # 查询每个chapter的数量
        cursor.execute(
            f"SELECT chapter, COUNT(*) AS count FROM exercise GROUP BY chapter"
        )
        
        # 获取结果
        results = cursor.fetchall()
        
        # 将结果转换为DataFrame并打印
        df = pd.DataFrame(results, columns=['Chapter', 'Count'])
        print(df)

    except Error as e:
        print(f"数据库错误: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# 调用函数
count_exercises_by_chapter(db_config)

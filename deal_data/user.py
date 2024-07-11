import csv
import mysql.connector
from mysql.connector import Error

# 读取CSV文件中的user_id列
user_ids = []
with open('./all_records.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        user_ids.append(row['user_id'])

# 去重
unique_user_ids = list(set(user_ids))

# 输出去重后的个数
print("去重后的个数:", len(unique_user_ids))


db_config = {
    'host': 'mysql.mysql',
    'database': 'sage_javon',
    'user': 'root',
    'password': 'pYRGObpCdG',
    'port': '3306'  # 默认MySQL端口
}


# MySQL表名
mysql_table = 'student'


try:
    # 连接MySQL数据库
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # 插入数据到 student 表
    for user_id in unique_user_ids:
        cursor.execute(
            'INSERT INTO student (id,nickname,gender) VALUES (%s,%s,%s)', (user_id, '学生'+user_id, 1))

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

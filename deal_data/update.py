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


def toggle_exercise_type(db_config):
    try:
        # 连接MySQL数据库
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # 更新type列，将0更新为1，将1更新为0
        sql_update_type_0_to_1 = "UPDATE exercise SET type = 1 WHERE id>213"

        cursor.execute(sql_update_type_0_to_1)
        # cursor.execute(sql_update_type_1_to_0)

        # 提交到数据库执行
        conn.commit()
        print("type列更新成功")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # 关闭数据库连接
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("数据库连接已关闭")


# 执行更新操作
toggle_exercise_type(db_config)

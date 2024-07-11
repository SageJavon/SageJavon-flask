import pandas as pd

# 读取CSV文件
df = pd.read_csv('./all_records.csv')

# 获取problem_id列的值
problem_ids = df['user_id']

# 初始化database_problem_id起始值
start_value = 1

# 遍历problem_id列，并修改database_problem_id列
current_database_id = start_value
for idx, problem_id in enumerate(problem_ids):
    if idx == 0:
        # 对第一行特殊处理，直接赋值起始值
        df.at[idx, 'database_user_id'] = current_database_id
    else:
        # 检查当前problem_id是否和上一个相同
        if problem_id != problem_ids[idx - 1]:
            # 如果不同，database_problem_id加一
            current_database_id += 1
        df.at[idx, 'database_user_id'] = current_database_id

# 将修改后的DataFrame保存回CSV文件
df.to_csv('output.csv', index=False)

print("CSV文件处理完成，并保存为output.csv")

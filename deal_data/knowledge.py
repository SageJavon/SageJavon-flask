# 定义两个txt文件路径
txt_file1 = './skill_names.txt'
txt_file2 = './skill_names_program.txt'

# 读取文件1的每一行内容
with open(txt_file1, 'r', encoding='utf-8') as f1:
    lines1 = f1.readlines()

# 读取文件2的每一行内容
with open(txt_file2, 'r', encoding='utf-8') as f2:
    lines2 = f2.readlines()

# 合并两个列表，并去重
combined_lines = list(set(lines1 + lines2))

# 将去重后的内容写入新的txt文件
output_file = 'combined_unique_lines.txt'
with open(output_file, 'w', encoding='utf-8') as fout:
    for line in combined_lines:
        fout.write(line)

print(f"Combined unique lines have been saved to '{output_file}'")

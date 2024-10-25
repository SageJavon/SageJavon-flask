# 定义文件路径
original_file = 'original_skills.txt'
choice_file = 'skills-choice.txt'
program_file = 'skills-program.txt'
output_file = 'updated_original_skills.txt'

def merge_skills(original_file, choice_file, program_file, output_file):
    # 读取 original_skills.txt 内容，保持顺序
    with open(original_file, 'r', encoding='utf-8') as f:
        original_skills = f.read().splitlines()  # 使用列表保持顺序
        original_skills_set = set(original_skills)  # 用于去重

    # 读取 skills-choice.txt 内容
    with open(choice_file, 'r', encoding='utf-8') as f:
        choice_skills = set(f.read().splitlines())  # 使用集合去重

    # 读取 skills-program.txt 内容
    with open(program_file, 'r', encoding='utf-8') as f:
        program_skills = set(f.read().splitlines())  # 使用集合去重

    # 合并 skills-choice 和 skills-program 的内容
    additional_skills = choice_skills.union(program_skills)

    # 去掉 original_skills.txt 中已经存在的知识点
    new_skills = additional_skills - original_skills_set

    # 把 original_skills.txt 中的内容保持不变，并追加新的知识点
    with open(output_file, 'w', encoding='utf-8') as f:
        for skill in original_skills:  # 写入原始内容，保持顺序
            f.write(skill + '\n')
        for skill in new_skills:  # 追加新的知识点
            f.write(skill + '\n')

    print(f"合并后的知识点已保存到 {output_file}")

# 执行合并操作
merge_skills(original_file, choice_file, program_file, output_file)

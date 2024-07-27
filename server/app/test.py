import os
import torch
import numpy as np

# 获取当前脚本的绝对路径
script_dir = os.path.dirname(__file__)

# 使用绝对路径加载模型和数据文件
question2idx_path = os.path.join(script_dir, 'data/question2idx.npy')
idx2question_path = os.path.join(script_dir, 'data/idx2question.npy')

print(question2idx_path)
print(idx2question_path)

question2idx = np.load(question2idx_path, allow_pickle=True).item()
idx2question = np.load(idx2question_path, allow_pickle=True).item()

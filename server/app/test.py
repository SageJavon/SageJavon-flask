import torch
import numpy as np
from scipy import sparse

question2idx = np.load('./data/question2idx.npy',
                       allow_pickle=True).item()
idx2question = np.load('./data/idx2question.npy',
                       allow_pickle=True).item()
model = torch.load(f='./model-100/result.pt')
qq_table = sparse.load_npz('./data/qq_table.npz').toarray()
qs_table = sparse.load_npz('./data/qs_table.npz').toarray()
ss_table = sparse.load_npz('./data/ss_table.npz').toarray()


print(model)
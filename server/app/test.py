import torch
import numpy as np
from scipy import sparse

model = torch.load(f='../app/model-100/result.pt')
question2idx = np.load('../app/data/question2idx.npy',
                       allow_pickle=True).item()
idx2question = np.load('../app/data/idx2question.npy',
                       allow_pickle=True).item()
model = torch.load(f='../app/model-100/result.pt')
qq_table = sparse.load_npz('../app/data/qq_table.npz').toarray()
qs_table = sparse.load_npz('../app/data/qs_table.npz').toarray()
ss_table = sparse.load_npz('../app/data/ss_table.npz').toarray()

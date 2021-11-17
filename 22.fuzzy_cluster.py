#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @ author: Koorye
# @ date: 2021-7-29
# @ function: 模糊聚类

# %%

import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage

# %%


# 距离公式
def dist(x, y):
	return np.sum(np.abs(x - y))

# 源数据
A = np.array([[5, 5, 3, 2],
              [2, 3, 4, 5],
              [5, 5, 2, 3],
              [1, 5, 3, 1],
              [2, 4, 5, 1]])

# 构造相似模糊矩阵
num = len(A)
R = np.zeros((num, num))
for i in range(len(A)):
	for j in range(len(A)):
		R[i, j] = 1 - .1 * dist(A[i, :], A[j, :])
print('R =\n',R)

# %%

# 平方法求传递闭包
def tr(R):
    R2 = R.copy()
    for row in range(len(R)):
        for col in range(len(R)):
            r_list = []
            for i in range(len(R)):
                r_list.append(np.min([R[row, i], R[i, col]]))
            R2[row, col] = np.max(r_list)
    return R2

R_old = R
R = tr(R)
while np.sum(np.abs(R-R_old)) > 1e-4:
    R_old = R
    R = tr(R)
print('t(R) =\n', R)

# %%

# 画聚类图
R2 = np.triu(1-R, 1)
R2 = R2[R2!=0]
Z = linkage(R2)
dendrogram(Z, labels=['I','II','III','IV','V'])

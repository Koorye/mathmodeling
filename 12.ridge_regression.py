#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @ author: Koorye
# @ date: 2021-7-26
# @ function: 使用 sklearn 进行岭回归

# %%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge, RidgeCV

# %%

# 源数据
df = pd.DataFrame({
    'x1': [7, 1, 11, 11, 7, 11, 3],
    'x2': [26, 29, 56, 31, 52, 55, 71],
    'y': [78.5, 74.3, 104.3, 87.6, 95.9, 109.2, 102.7],
})

X = np.array(df[['x1', 'x2']])
y = np.array(df[['y']])

# 遍历 k，计算不同 k 时的拟合结果
k_array = np.logspace(-4, 1.5, 100)
x1_list, x2_list = [], []
for k in k_array:
    model = Ridge(alpha=k).fit(X, y)
    x1_list.append(model.coef_[0][0])
    x2_list.append(model.coef_[0][1])

# %%

# 作岭迹图
plt.scatter(k_array,x1_list)
plt.scatter(k_array,x2_list)
plt.plot(k_array, x1_list, label='x1')
plt.plot(k_array, x2_list, label='x2')
plt.legend()

# %%

# 自动匹配最佳 k 值
model2 = RidgeCV().fit(X, y)

# %%

# 截距
b0 = model2.intercept_[0]

# 系数
b1, b2 = model2.coef_[0][0], model2.coef_[0][1]

print('y = {:.4f} + {:.4f}*x1 + {:.4f}*x2'.format(b0, b1, b2))
print('R_square =', model2.score(X, y))
print('k =', model2.alpha_)

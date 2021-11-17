#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @ author: Koorye
# @ date: 2021-7-26
# @ function: 使用 sklearn 进行多元线性回归

# %%

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# %%

# 源数据
df = pd.DataFrame({
    'x1': [7, 1, 11, 11, 7, 11, 3],
    'x2': [26, 29, 56, 31, 52, 55, 71],
    'y': [78.5, 74.3, 104.3, 87.6, 95.9, 109.2, 102.7],
})

X = np.array(df[['x1','x2']])
y = np.array(df[['y']])

# 多元线性回归模型
model = LinearRegression().fit(X, y)

# %%

# 截距
b0 = model.intercept_[0]

# 系数
b1, b2 = model.coef_[0]

print('y = {:.4f} + {:.4f}*x1 + {:.4f}*x2'.format(b0, b1,b2))
print('R_square =',model.score(X,y))
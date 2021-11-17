#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @ author: Koorye
# @ date: 2021-7-26
# @ function: 使用 sklearn 进行岭回归

# %%

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

# %%

# 源数据
df = pd.DataFrame({
    'good': [1, 1, 0, 0, 0, 1, 1],
    'sweet': [.95, .76, .82, .57, .69, .77, .89],
    'density': [.876, .978, .691, .745, .512, .856, 1.297],
    'volume': [1.85, 2.14, 1.34, 1.38, 0.67, 2.35, 1.69],
    'quality': [2.51, 2.45, 1.34, 1.15, 1.23, 3.95, 2.67],
})

# 样本集
X = np.array(df[df.columns[1:]])

# 标签集
y = np.array(df['good'])

# 建立模型
model = LogisticRegression()
model.fit(X, y)

# %%

# 截距
b0 = model.intercept_[0]

# 系数
b1, b2, b3, b4 = model.coef_[0][0], model.coef_[0][1], \
    model.coef_[0][2], model.coef_[0][3]

b0, b1, b2, b3, b4

# %%

# 预测
df2 = pd.DataFrame({
    'sweet': [.5, 1],
    'density': [.5, 1],
    'volume': [.5, 2],
    'quality': [.5, 2],
})
model.predict(np.array(df2))

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @ author: Koorye
# @ date: 2021-7-30
# @ function: Fisher 判别法

# %%

import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# %%

# 源数据
x0 = np.array([[1.24, 1.27],
              [1.36, 1.74],
              [1.38, 1.64],
              [1.38, 1.82],
              [1.38, 1.90],
              [1.14, 1.78],
              [1.18, 1.96],
              [1.20, 1.86],
              [1.26, 2.00],
              [1.28, 2.00]])

# 前 5 个属于 1 类 af，后 5 个属于 2 类 apf
label = np.array([1 for i in range(5)] + [2 for i in range(5)])

# 待判别数据
x = np.array([[1.24, 1.80]])

# %%

# 协方差矩阵
v = np.cov(x0.T)

# 模型

model = LinearDiscriminantAnalysis()
model.fit(x0, label)
model.predict(x)

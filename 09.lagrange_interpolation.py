#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @ author: Koorye
# @ date: 2021-7-26
# @ function: 使用 scipy 包进行拉格朗日插值

# %%

import numpy as np
from scipy.interpolate import lagrange

# %%

# 源数据
x = np.array([4, 5, 6])
y = np.array([10, 5.25, 1])

# 拉格朗日插值
poly = lagrange(x, y)
res = poly(18)

# %%

print('poly =\n', poly)
print('res =', res)

# %%

import matplotlib.pyplot as plt

# 画图
x1 = [i for i in range(-5,20)]
y1 = []
for each in x1:
	y1.append(poly(each))

plt.plot(x1, y1)
plt.scatter(x,y)
plt.scatter(18, res)

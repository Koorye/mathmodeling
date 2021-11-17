#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @ author: Koorye
# @ date: 2021-7-26
# @ function: 使用 scipy 包进行样条插值

# %%

import numpy as np
from scipy.interpolate import interp1d

# %%

# 原数据
x = np.array([1, 2, 5, 8, 9, 12, 15, 17])
y = np.array([4, 3, 7, 11, 5, 3, 13, 10])

# 一次、二次、三次样条插值
p1 = interp1d(x, y, kind='linear')
p2 = interp1d(x, y, kind='quadratic')
p3 = interp1d(x, y, kind='cubic')

# %%

# 画图
x1 = np.linspace(1, 17, 100)
y1 = p1(x1)
y2 = p2(x1)
y3 = p3(x1)

import matplotlib.pyplot as plt

plt.scatter(x,y)
plt.plot(x1,y1, label='linear')
plt.plot(x1,y2, label='quadratic')
plt.plot(x1,y3, label='cubic')
plt.legend()


# %%

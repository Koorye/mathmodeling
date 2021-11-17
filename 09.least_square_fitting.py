#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @ author: Koorye
# @ date: 2021-7-26
# @ function: 使用 numpy 包进行最小二乘拟合

# %%

import matplotlib.pyplot as plt
import numpy as np

# %%

# 源数据
x = np.array([1, 2, 3, 4])
y = np.array([4, 10, 18, 26])

# 多项式拟合
z1 = np.polyfit(x, y, 1)
z2 = np.polyfit(x, y, 2)
z3 = np.polyfit(x, y, 3)

p1 = np.poly1d(z1)
p2 = np.poly1d(z2)
p3 = np.poly1d(z3)

# %%

print('p1 =\n', p1)
print('p2 =\n', p2)
print('p3 =\n', p3)

# %%


x1 = np.linspace(-2, 7, 100)
y1 = p1(x1)
y2 = p2(x1)
y3 = p3(x1)
plt.scatter(x, y)
plt.plot(x1, y1, label='linear')
plt.plot(x1, y2, label='quadratic')
plt.plot(x1, y3, label='cubic')
plt.legend()

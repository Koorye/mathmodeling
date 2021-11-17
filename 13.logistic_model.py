#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @ author: Koorye
# @ date: 2021-7-27
# @ function: 使用 Logistic 模型拟合人口数据

# %%

import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

# %%

# 源数据
df = pd.DataFrame({
    'year': [1790, 1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870],
    'population': [3.9, 5.3, 7.2, 9.6, 12.9, 17.1, 23.2, 31.4, 38.6],
})

x0 = float(df['population'][0])
t0 = float(df['year'][0])

# %%

# Logistic 模型
def x(t, r, xm):
    return xm / (1 + (xm/x0-1)*np.exp(-r*(t-t0)))

# 拟合参数
popt, pcov = curve_fit(x,
                       df['year'].tolist(),
                       df['population'].tolist(),
                       bounds=((0, 1), (.1, np.inf)))
r, xm = popt[0], popt[1]
print('r =', r)
print('xm =', xm)

# 预测 1900 人口
print('population in 1900 =', x(1900, r, xm))

# %%

# 画出预测曲线
import matplotlib.pyplot as plt

year = np.linspace(1790,2000,21)
population = []
for each in year:
	population.append(x(each,r,xm))
plt.scatter(df['year'], df['population'], label='actual')
plt.plot(year, population, label='predict', color='coral')
plt.legend()
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @ author: Koorye
# @ date: 2021-7-29
# @ function: ARMA 模型

# %%

import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt

# %%

# 源数据
df = pd.DataFrame({
    'year': [i for i in range(1971, 1991)],
    'num': [66.6, 68.9, 38, 34.5, 15.5,
            12.6, 27.5, 92.5, 155.4, 154.6,
            140.4, 115.9, 66.6, 45.9, 17.9,
            3.4, 29.4, 100.2, 157.6, 142.6],
})

# %%

# 画 acf 图
plot_acf(df['num'])

# %%

# 画 pacf 图
plot_pacf(df['num'], lags=9)

# %%

# 建立模型，参考 acf、pacf 代入 p、q，观察 aic
str_list = []
for p in range(1, 6):
    for q in range(1, 3):
        model = sm.tsa.ARMA(df['num'], (p, q)).fit()
        str_list.append('p = {}, q = {}, aic = {}'.format(p, q, model.aic))

for each in str_list:
	print(each)

# %%

# 发现 p=2,q=2 时 aic 最小，取 p=2,q=2
model = sm.tsa.ARMA(df['num'], (2, 2)).fit()
model.summary()

# %%

# 预测和画图
plt.plot(df['year'], df['num'])
plt.scatter(df['year'], df['num'], label='actual')
year_list = [i for i in range(1971, 2001)]
plt.plot(year_list, model.predict(0, len(year_list)-1))
plt.scatter(year_list, model.predict(0, len(year_list)-1), label='predict')
plt.legend()

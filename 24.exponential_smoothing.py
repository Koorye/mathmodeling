#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @ author: Koorye
# @ date: 2021-7-29
# @ function: 指数平滑法

# %%

import numpy as np
import pandas as pd

# %%

# 源数据
df = pd.DataFrame({
    't': [i for i in range(1, 11)],
    'production': [2031, 2234, 2566, 2820, 3006,
                   3093, 3277, 3514, 3770, 4107],
})

# 设 alpha=.3，计算一次、二次指数平滑
alpha = .3
s1, s2 = [int(df['production'][0])],\
    [int(df['production'][0])]

for i in range(1, len(df['t'])):
	s1.append(alpha*df['production'][i] + (1-alpha)*s1[i-1])
	s2.append(alpha*s1[i] + (1-alpha)*s2[i-1])
df['s1'] = s1
df['s2'] = s2

# %%

# 计算过去年的预测值，以及未来年的线性表达式
predict_list = [None]
for i in range(len(df['t'])-1):
	a = 2*df['s1'][i] - df['s2'][i]
	b = (alpha / (1-alpha)) * (df['s1'][i] - df['s2'][i])
	predict_list.append(a + b)

t = 10
a = 2*df['s1'][t-1] - df['s2'][t-1]
b = (alpha / (1-alpha)) * (df['s1'][t-1] - df['s2'][t-1])
df['predict'] = predict_list
print('at =', a)
print('bt =', b)

# %%

# 计算未来年的预测值
pred_df = df.copy()
for i in range(5):
	pred_df = pd.concat([pred_df, pd.DataFrame({
		't': [10+i+1],
		'predict': a + b*i,
	})])
pred_df

# %%

# 画图
import matplotlib.pyplot as plt

plt.plot(pred_df['t'], pred_df['production'],label='production')
plt.scatter(pred_df['t'], pred_df['production'])
plt.plot(pred_df['t'], pred_df['s1'],label='s1')
plt.scatter(pred_df['t'], pred_df['s1'])
plt.plot(pred_df['t'], pred_df['s2'],label='s2')
plt.scatter(pred_df['t'], pred_df['s2'])
plt.plot(pred_df['t'], pred_df['predict'],label='predict')
plt.scatter(pred_df['t'], pred_df['predict'])
plt.legend()
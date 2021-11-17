#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @ author: Koorye
# @ date: 2021-7-28
# @ function: Lesile 模型

# %%

import numpy as np

# %%

# 源数据
alpha = np.array([0, 4, 3])
beta = np.array([.5, .25])

L = np.zeros((len(alpha), len(alpha)))
L[0, :] = alpha
for index, each in enumerate(beta):
    L[index+1, index] = each

x0 = np.array([1000, 1000, 1000])

# 迭代求解
x_list = [x0]
for i in range(5):
    x_list.append(L.dot(x_list[-1].T))
for index, x in enumerate(x_list):
    print('the {}th year: 1y: {}, 2y: {}, 3y: {}'.format(
        index, x[0], x[1], x[2]))

# %%

import matplotlib.pyplot as plt

year_list = np.array(range(len(x_list)))
y1,y2,y3 = [],[],[]
for year in year_list:
	y1.append(x_list[year][0])
	y2.append(x_list[year][1])
	y3.append(x_list[year][2])

w = .3
plt.bar(year_list-w,y1, width=w, label='1y')
plt.bar(year_list,y2, width=w, label='2y')
plt.bar(year_list+w,y3, width=w, label='3y')
plt.legend()

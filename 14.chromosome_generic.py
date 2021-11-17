#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @ author: Koorye
# @ date: 2021-7-28
# @ function: 染色体遗传模型

# %%

import numpy as np

# %%

# 都选用 AA 结合    
M1 = np.array([[1, .5, 0],
               [0, .5, 1],
               [0, 0, 0]])

# 选用相同基因组结合
M2 = np.array([[1, .25, 0],
               [0, .5, 0],
               [0, .25, 1]])

x0 = np.array([1/3, 1/3, 1/3])

# 迭代求解
x1_list, x2_list = [x0], [x0]
for i in range(10):
	x1_list.append(M1.dot(x1_list[-1].T))
	x2_list.append(M2.dot(x2_list[-1].T))

print('----- M1 -----')
for index, each in enumerate(x1_list):
	print('iter {}: AA: {:.4f}, Aa: {:.4f}, aa: {:.4f}'.format(index, each[0], each[1], each[2]))

print('\n----- M2 -----')
for index, each in enumerate(x2_list):
	print('iter {}: AA: {:.4f}, Aa: {:.4f}, aa: {:.4f}'.format(index, each[0], each[1], each[2]))


# %%

# 情况一画图
a,b,c = [], [], []
for each in x1_list:
	a.append(each[0])
	b.append(each[1])
	c.append(each[2])

import matplotlib.pyplot as plt

it = [i for i in range(11)]
plt.plot(it,a)
plt.plot(it,b)
plt.plot(it,c)
plt.scatter(it,a, label='AA')
plt.scatter(it,b, label='Aa')
plt.scatter(it,c, label='aa')
plt.legend()

# %%

# 情况二画图
a,b,c = [], [], []
for each in x2_list:
	a.append(each[0])
	b.append(each[1])
	c.append(each[2])

import matplotlib.pyplot as plt

it = [i for i in range(11)]
plt.plot(it,a, alpha=.5)
plt.plot(it,b)
plt.plot(it,c, alpha=.5)
plt.scatter(it,a, label='AA', alpha=.5)
plt.scatter(it,b, label='Aa')
plt.scatter(it,c, label='aa', alpha=.5)
plt.legend()
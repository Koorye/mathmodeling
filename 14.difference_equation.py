#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @ author: Koorye
# @ date: 2021-7-28
# @ function: 使用 sympy 求解差分方程

# %%

import numpy as np
import sympy as sp

# %%

# 定义方程
x = sp.symbols('x')
y = sp.Function('y')
f = y(x+2) - y(x+1) - y(x)

con = {
	y(1):1,
	y(2):1,
}

# 解递归方程
solve = sp.rsolve(f, y(x), con)
solve

# %%

# 画图
x1 = np.linspace(1,10,10)
y1 = []
for each in x1:
	y1.append((solve.subs(x,each).evalf()))
y1

import matplotlib.pyplot as plt

plt.plot(x1,y1)
plt.scatter(x1,y1)

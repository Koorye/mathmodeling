#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @ author: Koorye
# @ date: 2021-7-27
# @ function: 使用 scipy、sympy 求微分方程的数值解、解析解

# %%

import numpy as np
from scipy.integrate import odeint
from sympy import *

# %%

# 使用 scipy 求数值解
# 微分方程
dy = lambda y,x:-2*y + x**2 + 2*x

# 数值范围
x1 = np.linspace(1,10,20)

# 求数值解，y 的初始值为 2
y1 = odeint(dy, 2, x1)
y1

# %%

# 使用 sympy 求解析解

# 定义变量和函数
x = symbols('x', real=True)
y = Function('y')

# 定义方程和约束
eq = y(x).diff(x) + 2*y(x) - x**2 - 2*x
con = {
	y(1): 2,
}

# 求解
f = simplify(dsolve(eq, ics=con))
f

# %%

# 向解中代入不同的值
x2 = np.linspace(1,10,100)
y2 = []
for each in x2:
	y2.append(list(sorted(f.subs(x,each).evalf().atoms()))[1])

# %%

# 画图
import matplotlib.pyplot as plt

plt.scatter(x1,y1, label='x1', color='coral')
plt.plot(x2,y2, label='x2')
plt.legend()

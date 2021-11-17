#! /usr/bin/env python
# -*- coding: utf-8 -*-
#@ author: Koorye
#@ date: 2021-7-23
#@ function: 使用 cvxpy 包进行非线性规划问题求解

# %%

import numpy as np
import cvxpy as cp

# %%

# 目标函数的平方项
c1 = np.array([1, 1, 3, 4, 2])

# 目标函数的一次项
c2 = np.array([-8, -2, -3, -1, -2])

# 约束项
a = np.array([[1, 1, 1, 1, 1],
              [1, 2, 2, 1, 6],
              [2, 1, 6, 0, 0],
              [0, 0, 1, 1, 5]])
b = np.array([400, 800, 200, 200])

# 决策变量
x = cp.Variable(5, integer=True)

# 目标函数
obj = cp.Minimize(c1 @ x**2 + c2 @ x)

# 约束
con = [0 <= x, x <= 99, a@x <= b]

# 问题模型
prob = cp.Problem(obj, con)
prob.solve(solver='ECOS_BB')

# %%

print('best z =', prob.value)
print('best x =', x.value)

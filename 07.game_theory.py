#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @ author: Koorye
# @ date: 2021-7-25
# @ function: 使用 cvxpy 包进行矩阵对策混合策略求解

# %%

import numpy as np
import cvxpy as cp

# %%

# 赢得矩阵
A = np.array([[3, 0, 2, 0],
              [0, 2, 1, 5],
              [1, 2, 3, 4]])

# %%

# 不等式约束形如 A * x <= b
A1 = A.copy().T
A2 = A.copy()

# 决策变量
x = cp.Variable(A1.shape[1]+1)
y = cp.Variable(A2.shape[1]+1)

# 约束条件
con1 = [
    A1 @ x[:-1] >= x[-1],
    sum(x[:-1]) == 1,
    x[:-1] >= 0,
]
con2 = [
    A2 @ y[:-1] <= y[-1],
    sum(y[:-1]) == 1,
    y[:-1] >= 0,
]

# 目标函数
obj1 = cp.Maximize(x[-1])
obj2 = cp.Minimize(y[-1])

# %%

p1 = cp.Problem(obj1, con1)
p2 = cp.Problem(obj2, con2)
p1.solve(solver='GLPK_MI', verbose=True)
p2.solve(solver='GLPK_MI', verbose=True)

# %%

print('x =', x.value[:-1])
print('y =', y.value[:-1])
print('x exp =', x.value[-1])
print('y exp =', y.value[-1])

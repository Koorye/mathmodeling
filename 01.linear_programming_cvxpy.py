#! /usr/bin/env python
# -*- coding: utf-8 -*-
#@ author: Koorye
#@ date: 2021-7-23
#@ function: 使用 cvxpy 包进行线性规划问题求解

# %%

import numpy as np
import cvxpy as cp

# %%

# 目标函数形如 min c^T·x
c = np.array([2, 3, -5])

# 不等式约束形如 A·x <= b
A = np.array([[-2, 5, -1],
              [1, 3, 1]])
b = np.array([-10, 12])

# 等式约束形如 Aeq·x = beq
Aeq = np.array([[1, 1, 1]])
beq = np.array([7])

# 取值范围约束形如 lb <= x <= ub
lb = np.array([0, 0, 0])

x = cp.Variable(3)
con = [
    A * x <= b,
    Aeq * x == beq,
    x >= lb,
]
z = cp.Minimize(c * x)

# %%

p = cp.Problem(z, con)
p.solve(solver='GLPK_MI', verbose=True)

# %%

print('x =', x.value)
print('y =', p.value)


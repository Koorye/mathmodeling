#! /usr/bin/env python
# -*- coding: utf-8 -*-
#@ author: Koorye
#@ date: 2021-7-23
#@ function: 使用 scipy 包进行线性规划问题求解

# %%

import numpy as np
from scipy.optimize import linprog

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
ub = np.array([None, None, None])
bound = tuple(zip(lb, ub))

res = linprog(c, A, b, Aeq, beq, bound)
print('min y =', res.fun)
print('x =', res.x)
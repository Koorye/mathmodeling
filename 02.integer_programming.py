#! /usr/bin/env python
# -*- coding: utf-8 -*-
#@ author: Koorye
#@ date: 2021-7-23
#@ function: 使用 cvxpy 包进行整数线性规划问题求解

# %%

import numpy as np
import cvxpy as cp

# %%

# 目标函数形如 min c^T·x
c = np.array([40, 90])

# 约束形如 a·x <= b
a = np.array([[9, 7],
              [-7, -20]])
b = np.array([56, -70])

# 两个整数决策变量
x = cp.Variable(2, integer=True)

# 目标函数
z = cp.Minimize(c * x)

# 约束条件
cons = [a * x <= b,
        x >= 0]

# 问题模型
prob = cp.Problem(z, cons)
prob.solve(solver='GLPK_MI', verbose=True)

# %%

print('best z =', prob.value)
print('best x =', x.value)

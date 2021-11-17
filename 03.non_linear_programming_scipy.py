#! /usr/bin/env python
# -*- coding: utf-8 -*-
#@ author: Koorye
#@ date: 2021-7-23
#@ function: 使用 scipy 包进行非线性规划问题求解

# %%

import cvxpy as cp
import numpy as np
from scipy.optimize import minimize

# %%

# 目标函数


def obj(x):
    x1, x2, x3 = x
    return (2+x1)/(1+x2)-3*x1+4*x3


# 取值范围
bound = [(.1, .9) for _ in range(3)]
res = minimize(obj, np.ones(3), bounds=bound)

# %%

print('best obj =', res.fun)
print('success =', res.success)
print('best x =', res.x)


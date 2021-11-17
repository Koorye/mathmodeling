#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @ author: Koorye
# @ date: 2021-7-26
# @ function: 使用 statsmodels 进行多元线性回归

# %%

import numpy as np
import pandas as pd
from statsmodels.formula.api import ols

# %%

# 源数据
dic = {
    'x1': [7, 1, 11, 11, 7, 11, 3],
    'x2': [26, 29, 56, 31, 52, 55, 71],
    'y': [78.5, 74.3, 104.3, 87.6, 95.9, 109.2, 102.7],
}

# 建立最小二乘拟合模型
model = ols('y~x1+x2', dic).fit()

# %%

# 概述
model.summary()

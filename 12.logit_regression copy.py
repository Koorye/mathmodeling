#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @ author: Koorye
# @ date: 2021-7-26
# @ function: 使用 sklearn 进行岭回归

# %%

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

# %%

# 源数据
df = pd.DataFrame({
    'good': [1, 1, 0, 0, 0, 1, 1],
    'sweet': [.95, .76, .82, .57, .69, .77, .89],
    'density': [.876, .978, .691, .745, .512, .856, 1.297],
    'volume': [1.85, 2.14, 1.34, 1.38, 0.67, 2.35, 1.69],
    'quality': [2.51, 2.45, 1.34, 1.15, 1.23, 3.95, 2.67],
})

# 建立模型
model = smf.logit('good~sweet+density+volume+quality', df)

# %%

res = model.fit(method='cg')
res.summary()

# %%

df2 = pd.DataFrame({
    'good': [None, None],
    'sweet': [.5, 1],
    'density': [.5, 1],
    'volume': [.5, 2],
    'quality': [.5, 2],
})
res.predict(df2)
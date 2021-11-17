#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @ author: Koorye
# @ date: 2021-7-30
# @ function: 主成分分析

# %%

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

# %%

# 源数据
df = pd.DataFrame({
    'x1': [149.5, 162.5, 162.7, 162.2, 156.5],
    'x2': [69.5, 77, 78.5, 87.5, 74.5],
    'x3': [38.5, 55.5, 50.8, 65.5, 49]
})

# 模型
model = PCA().fit(np.array(df))

# %%

print('特征值:', model.explained_variance_)
print('贡献率:', model.explained_variance_ratio_)
print('各主成分的系数:', model.components_)

# %%

pca_df = pd.DataFrame(model.transform(np.array(df)))
pca_df.columns = ['F1', 'F2', 'F3']
pca_df

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @ author: Koorye
# @ date: 2021-7-30
# @ function: K 均值聚类

# %%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# %%

# 源数据
df = pd.DataFrame(load_iris()['data'], columns=load_iris()['feature_names'])

# 计算 k 取不同值时的轮廓系数
score_list = []
for i in range(2,10):
    model = KMeans(i)
    model.fit(df.iloc[:,:2])
    score_list.append(silhouette_score(df, model.labels_))

plt.plot([i for i in range(2,10)], score_list)

# %%

model = KMeans(3)
model.fit(df.iloc[:,:2])
df2 = df.iloc[:,:2].copy()
df2['label'] = model.labels_

from plotnine import *

(
    ggplot(df2,aes('sepal length (cm)', 'sepal width (cm)', color='label'))
    + geom_point()
    + theme_matplotlib()
)

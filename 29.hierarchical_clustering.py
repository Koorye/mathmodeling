#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @ author: Koorye
# @ date: 2021-7-30
# @ function: 层次聚类

# %%

import numpy as np
import pandas as pd
import scipy.cluster.hierarchy as sch

# %%

# 源数据
df = pd.DataFrame({
	'Cu': [2.9909,3.2044,2.8392,2.5315,2.5897,2.9600,3.1184],
	'W':[.3111,.5348,.5696,.4528,.3010,3.0480,2.8395],
	'Mo': [.5324,.7718,.7614,.4893,.2735,1.4997,1.9350],
})

# 计算两两距离
dist = sch.distance.pdist(df)

# 转化为距离矩阵
dist_mat = sch.distance.squareform(dist)

# 聚类并画图
z = sch.linkage(dist)
sch.dendrogram(z)

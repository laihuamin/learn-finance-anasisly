#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
#
#
# stock_0 = 'sz000001'
#
# def get_lrb(stock_id):
#     lrb = pd.read_csv(
#         stock_id + '_lrb.csv',
#         encoding='utf-8',
#         header=0
#     )
#     return lrb
#
# # 获取到lrb
# lrb = get_lrb(stock_0)
# print(pd.__version__)
#
# def get_timeend(lrb):
#     list = np.array(lrb[u'报表期截止日'].tolist())
#     return list
# list_time_end = get_timeend(lrb)

# list = []
#     # 获取每一列的数据，根据截止日期去对应每个数据
#     for i in lrb.columns:
#         list.append(np.array(lrb[i]).tolist())
#     return list

obj = pd.Series([1, 2, 3, 4])
print obj
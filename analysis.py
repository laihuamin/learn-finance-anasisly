#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

stock_0 = 'sz000001'

year = 2018

def get_all_data(stock_id):
    lrb = pd.read_csv(
        stock_id + '_lrb.csv',
        encoding='utf-8',
        header=0,
    )
    list_lrb = []
    for i in lrb[u'报表期截止日']:
        str_i = str(i)
        list_lrb.append(str_i)
    list_lrb_0 = []
    for i in list_lrb:
        i_ = i[:4] + '-' + i[4:6] + '-' + i[6:8]
        list_lrb_0.append(i_)

    lrb[u'报告时间'] = [pd.to_datetime(t) for t in list_lrb_0]

    lrb.index = lrb[u'报告时间']
    data = lrb[::-1]
    return data

def get_data_month(data, month):
    print(data.index.month)
    data_month = data[data.index.month == month]
    return data_month

def get_data_ratio(data, i):
    result = pd.DataFrame()

    result['Operating_income_' + i] = data[u'一、营业收入']
    # result['归母净利润'] = data[u'归属于母公司的净利润']
    # result['营业利润'] = data['营业利润']
    # result['营业利润率'] = data['营业利润'] / data[u'一、营业收入']
    # result['净利率'] = data['归属于母公司所有者的净利润'] / data['营业收入']
    # result['毛利率'] = (data['营业收入'] - data['营业成本']) / data['营业收入']
    result.index = data[u'报告时间']
    return result


# 根据数据进行作图
def data_plot(data, ratio, legend='Ping-An Bank', kind='bar'):
    l_0 = len(data)
    s_0 = list(range(l_0))
    x_0 = np.array(s_0)
    y_0 = tuple([str(i) for i in range(year - l_0, year)])
    data[ratio].plot(kind=kind)
    plt.title('%s' % (ratio))
    plt.legend([legend])
    plt.xticks(x_0, y_0)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.4)
    # plt.savefig('%s.png' % (ratio))
    return

    # data = get_all_data(stock_0)
    # data_year = get_data_month(data, int(i))
    # result = get_data_ratio(data_year, i)
    # data_plot(result, 'Operating_income_' + i)

# plt.show()


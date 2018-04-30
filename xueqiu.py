# coding: utf-8
# import pandas as pd
# import requests
# from multiprocessing.dummy import Pool as ThreadPool
#
# lrb_base_url = 'http://api.xueqiu.com/stock/f10/incstatement.csv?page=1&size=10000&symbol='
#
# headers = {
#     'User-Agent': 'Mozilla/5.0',
#     'Cookie': 'xq_a_token=4c6af5a6a2c8e7862e51b7761695e6e88e768a3'
# }
#
# def download_lrb(url):
#     r = requests.get(url, headers=headers)
#     filename = url.split('=')[-1] + '_lrb.csv'
#     print(filename)
#     with open(filename, 'wb') as f:
#         f.write(r.content)
#
#
# symbol = ['SZ000001']
#
# lrb_urls = [lrb_base_url + i for i in symbol]
#
# pool = ThreadPool(10)
# pool.map(download_lrb, lrb_urls)
# pool.close()
# pool.join()

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
    data_month = data[data.index.month == month]
    return data_month

def get_data_ratio(data):
    result = pd.DataFrame()

    result['Operating_income'] = data[u'一、营业收入']
    # result['归母净利润'] = data[u'归属于母公司的净利润']
    # result['营业利润'] = data['营业利润']
    # result['营业利润率'] = data['营业利润'] / data[u'一、营业收入']
    # result['净利率'] = data['归属于母公司所有者的净利润'] / data['营业收入']
    # result['毛利率'] = (data['营业收入'] - data['营业成本']) / data['营业收入']
    result.index = data[u'报告时间']
    return result


# 根据数据进行作图
def data_plot(data, ratio, legend='平安银行', kind='bar'):
    l_0 = len(data)
    s_0 = list(range(l_0))
    x_0 = np.array(s_0)
    y_0 = tuple([str(i) for i in range(year - l_0, year)])

    data[ratio].plot(kind=kind)
    plt.title('%s' % (ratio))
    plt.legend([legend])
    plt.xticks(x_0, y_0)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.4)
    plt.savefig('%s.png' % (ratio))
    return

data = get_all_data(stock_0)
data_year = get_data_month(data, 3)
result = get_data_ratio(data_year)
print(result)
data_plot(result, 'Operating_income')

plt.show()

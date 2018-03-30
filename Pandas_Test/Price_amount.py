# -*- coding: utf-8 -*-


import numpy as  np
import pandas as pd
import os
import matplotlib


def get_csv(filename):
    '''
    读取目标文件
    :param filename:
    :return:
    '''
    path = os.getcwd()
    csv = pd.read_csv(path + '\\'+filename)
    return csv

def get_time_price(csv):
    '''
    获得订单的时间-价钱的数据
    :param csv:
    :return:
    '''
    csv_new = csv[csv['transaction-type'] == 'Order']
    csv_time_price = csv_new[['posted-date', 'price-amount']]
    # 去掉缺失值,并根据时间排序
    csv_time_price = csv_time_price.dropna().sort_values('posted-date')


    return csv_time_price

def get_day_order(csv):
    '''
    清洗日期格式，并累加同一天的销售数量
    :param csv:
    :return:
    '''
    csv_order = csv[csv['transaction-type'] == 'Order']
    csv_day_order = csv_order[['posted-date', 'quantity-purchased']]
    # 处理缺失值
    csv_day_order = csv_day_order.dropna()

    # 处理时间数据，生成新的CSV数据表
    # T = pd.DataFrame([i[:10] for i in csv_day_order['posted-date']], index= csv_day_order.index)
    # 第二种更快的，处理时间数据，生成新的CSV数据表
    t = pd.Series(pd.to_datetime(csv_day_order['posted-date'],))
    # 第一种
    # csv_day_order['posted-date'] = T
    # 第二种
    csv_day_order['posted-date'] = t.dt.date

    csv_day_order.rename(columns={'quantity-purchased': u'订单量', 'posted-date': u'时间'}, inplace=True)
    # 将同一天的销售量累加
    csv_day_order = csv_day_order.groupby(u'时间').sum()

    drawing(csv_day_order,title=u'每日订单量',color='red')
    return csv_day_order

def get_day_sku(csv,sku_name):
    '''
    获得单独的sku系列每日订单量数据
    :param csv:
    :param sku_name:
    :return:
    '''
    csv_sku = csv[csv['transaction-type'] == 'Order']
    csv_day_sku = csv_sku[['posted-date', 'sku','quantity-purchased']]
    # 处理缺失值
    csv_day_sku = csv_day_sku.dropna()
    # 处理时间数据，生成新的CSV数据表
    t = pd.Series(pd.to_datetime(csv_day_sku['posted-date'], ))
    csv_day_sku['posted-date'] = t.dt.date
    # 使用模糊分别匹配sku
    r = r'%s' % sku_name
    data = csv_day_sku['sku']
    data = data[data.str.contains(r,na = True)]
    csv_day_sku['nid'] = data
    csv_day_sku = csv_day_sku.dropna()
    print(csv_day_sku)
    # 修改列名字
    csv_day_sku.rename(columns={'quantity-purchased':sku_name+u'系列','posted-date':u'时间'}, inplace=True)
    # 求和
    csv_day_sku = csv_day_sku[[u'时间',sku_name+u'系列']].groupby(u'时间').sum()
    # 调用绘图函数
    drawing(csv_day_sku,title=u'%s系列每日订单量'%sku_name)
    return (csv_day_sku)

def get_day_sku_all(csv,sku_name_list):
    '''
    传入总CSV，整合sku系列订单量
    :param csv: 总数据
    :param sku_name_list:sku系列名，列表
    :return:
    '''
    csv_sku = csv[csv['transaction-type'] == 'Order']
    csv_sku_all = csv_sku[['posted-date', 'sku','quantity-purchased']]
    # 去重
    # csv_day_sku = csv_day_sku.drop_duplicates()
    # 处理缺失值
    csv_sku_all = csv_sku_all.dropna()
    # 处理时间数据，生成新的CSV数据表
    t = pd.Series(pd.to_datetime(csv_sku_all['posted-date'], ))
    csv_sku_all['posted-date'] = t.dt.date

    sku_list = []
    for sku_name in sku_name_list:
        csv_day_sku = csv_sku_all
        # 使用模糊分别匹配sku
        r = r'%s' % sku_name
        data = csv_day_sku['sku']
        data = data[data.str.contains(r,na = True)]
        csv_day_sku['nid'] = data
        csv_day_sku = csv_day_sku.dropna()
        # 修改列名字
        csv_day_sku.rename(columns={'quantity-purchased':sku_name+u'系列','posted-date':u'时间'}, inplace=True)
        # 求和
        csv_day_sku = csv_day_sku[[u'时间',sku_name+u'系列']].groupby(u'时间').sum()
        sku_list.append(csv_day_sku)
    # 合并数据
    res = pd.concat(sku_list, axis=1)
    drawing(res)
    return (res)

# 导入绘图库
import matplotlib.pyplot as plt
def drawing(csv,title=u'数据分析',color = None,figsize = (6,6),linewidth = 1.5,alpha = 0.8):
    '''
    pandas绘图接口
    :param csv:
    :return:
    '''
    # 设置中文字体
    matplotlib.rc('font', **{'family': 'SimHei'})
    # 自定义颜色
    # if type(csv) == list:
    #     plt.plot(csv[u'YSW5402系列'], 'g-', csv[u'YSW1623系列'], 'r-')
    csv.plot(color = color,linewidth = linewidth , linestyle = '-' , title = title, alpha = alpha,rot=45,
             figsize = figsize,fontsize = 7)
    if type(csv) == list:
        plt.savefig('%s.jpg' % title)
    elif type(csv) == type(pd.DataFrame()):
        plt.savefig('%s.jpg' % title)
    plt.show()


if __name__ == '__main__':

    filename = '0211-0225bak.csv'
    csv = get_csv(filename)
    # csv_day_order = get_day_order(csv)
    # csv_day_sku = get_day_sku(csv,'YSW5402')
    # csv_day_sku = get_day_sku(csv,'YSW1623')
    sku_list = get_day_sku_all(csv,['YSW5402','YSW1623','YSK37509','YSW1610','YSW7603','YSW8004'])


# -*- coding: utf-8 -*-

import time
import numpy as  np
import pandas as pd
import os
import matplotlib
# 导入绘图库
import matplotlib.pyplot as plt

def get_csv(filename):
    '''
    读取目标文件
    :param filename:
    :return:
    '''
    path = os.getcwd()
    csv = pd.read_csv(path + '\\'+filename)
    return csv

######   这是一开始写的函数，发现很多代码重复，一开始思路就不正确，应该先总体清洗出有用的数据返回，再进行处理 #####@
# def get_day_order(csv):
#     '''
#     清洗日期格式，并累加同一天的销售数量
#     :param csv:
#     :return:
#     '''
#     csv_order = csv[csv['transaction-type'] == 'Order']
#     csv_day_order = csv_order[['posted-date', 'quantity-purchased']]
#     # 处理缺失值
#     csv_day_order = csv_day_order.dropna()
#
#     # 处理时间数据，生成新的CSV数据表
#     # T = pd.DataFrame([i[:10] for i in csv_day_order['posted-date']], index= csv_day_order.index)
#     # 第二种更快的，处理时间数据，生成新的CSV数据表
#     t = pd.Series(pd.to_datetime(csv_day_order['posted-date'],))
#     # 第一种
#     # csv_day_order['posted-date'] = T
#     # 第二种
#     csv_day_order['posted-date'] = t.dt.date
#
#     csv_day_order.rename(columns={'quantity-purchased': u'订单量', 'posted-date': u'时间'}, inplace=True)
#     # 将同一天的销售量累加
#     csv_day_order = csv_day_order.groupby(u'时间').sum()
#
#     drawing(csv_day_order,title=u'每日订单量',color='red')
#     return csv_day_order


# def get_day_sku(csv,sku_name):
#     '''
#     获得单独的sku系列每日订单量数据
#     :param csv:
#     :param sku_name:
#     :return:
#     '''
#     csv_sku = csv[csv['transaction-type'] == 'Order']
#     csv_day_sku = csv_sku[['posted-date', 'sku','quantity-purchased']]
#     # 处理缺失值
#     csv_day_sku = csv_day_sku.dropna()
#     # 处理时间数据，生成新的CSV数据表
#     t = pd.Series(pd.to_datetime(csv_day_sku['posted-date'], ))
#     csv_day_sku['posted-date'] = t.dt.date
#     # 使用模糊分别匹配sku
#     r = r'%s' % sku_name
#     data = csv_day_sku['sku']
#     data = data[data.str.contains(r,na = True)]
#     csv_day_sku['nid'] = data
#     csv_day_sku = csv_day_sku.dropna()
#
#     # 修改列名字
#     csv_day_sku.rename(columns={'quantity-purchased':sku_name,'posted-date':u'时间'}, inplace=True)
#     # 求和
#     csv_day_sku = csv_day_sku[[u'时间',sku_name]].groupby(u'时间').sum()
#     # 调用绘图函数
#     drawing(csv_day_sku,title=u'%s系列每日订单量'%sku_name)
#     return (csv_day_sku)
#
# def get_day_sku_all(csv,sku_name_list):
#     '''
#     传入总CSV，整合sku系列订单量
#     :param csv: 总数据
#     :param sku_name_list:sku系列名，列表
#     :return:
#     '''
#     csv_sku = csv[csv['transaction-type'] == 'Order']
#     csv_sku_all = csv_sku[['posted-date', 'sku','quantity-purchased']]
#     # 去重
#     # csv_day_sku = csv_day_sku.drop_duplicates()
#     # 处理缺失值
#     csv_sku_all = csv_sku_all.dropna()
#     # 处理时间数据，生成新的CSV数据表
#     t = pd.Series(pd.to_datetime(csv_sku_all['posted-date'], ))
#     csv_sku_all['posted-date'] = t.dt.date
#
#     sku_list = []
#     for sku_name in sku_name_list:
#         csv_day_sku = csv_sku_all
#         # 使用模糊分别匹配sku
#         r = r'%s' % sku_name
#         data = csv_day_sku['sku']
#         data = data[data.str.contains(r,na = True)]
#         csv_day_sku['nid'] = data
#         csv_day_sku = csv_day_sku.dropna()
#         # 修改列名字
#         csv_day_sku.rename(columns={'quantity-purchased':sku_name,'posted-date':u'时间'}, inplace=True)
#         # 求和
#         csv_day_sku = csv_day_sku[[u'时间',sku_name]].groupby(u'时间').sum()
#         sku_list.append(csv_day_sku)
#
#     # 合并数据
#     res = pd.concat(sku_list, axis=1)
#     drawing(res,title=u'每日销售走势图')
#     return (res)

def get_sku_info_dict(csv,sku_name_list):
    '''
    获得sku信息字典
    :param csv:
    :param sku_name:
    :return:
    '''
    csv_order_info = csv[csv['transaction-type'] == 'Order']
    sku_info_all = csv_order_info[['posted-date', 'quantity-purchased', 'price-amount', 'item-related-fee-amount', 'sku']]
    # 将缺失值填充
    _ = sku_info_all.fillna(0, inplace=True)

    sku_info_dict = {}
    # 模糊匹配
    for sku_name in sku_name_list:
        sku_info = sku_info_all
        r = r'%s' % sku_name
        data = sku_info['sku']
        data = data[data.str.contains(r, na=True)]
        sku_info['nid'] = data
        sku_info = sku_info.dropna()
        # 价格合并到一起
        amount = sku_info[[ 'price-amount', 'item-related-fee-amount']]
        amount['sum'] = amount.apply(lambda x: x.sum(), axis=1)
        sku_info['sum'] = amount['sum']
        # 处理时间数据，生成新的CSV数据表
        t = pd.Series(pd.to_datetime(sku_info['posted-date'], ))
        sku_info['posted-date'] = t.dt.date
        # 得到每日订单数/总金额/其他费用
        sku_info = sku_info.groupby('posted-date').sum()
        sku_info_dict['%s'% sku_name] = sku_info
    return sku_info_dict


def get_diagram_day_sku_list(sku_info_dict,sku_name_list):
    '''
    传入一个想查询的列表名，获得关系图
    :param sku_info_dict:
    :param sku_name_list:
    :return:
    '''
    sku_list = []
    for sku_name in sku_name_list:
        data = sku_info_dict['%s' % sku_name]['quantity-purchased']
        # DataFrame存入字典后取出变成series，故需要转回DataFrame，顺便设置列名
        data  = data.to_frame(name=sku_name)
        sku_list.append(data)
    # 合并数据
    data = pd.concat(sku_list, axis=1)
    # 绘图
    drawing(data,title=u'每日订单数量走势图')
    return (data)


def get_sku_info(sku_info_dict,sku_name):
    '''
    根据名字获取sku中想要的系列
    :param sku_info_dict:
    :param sku_name:
    :return:
    '''
    sku_info  = sku_info_dict['%s' % sku_name]
    return sku_info


def get_average_price_quantity_purchased(sku_info_dict,sku_name):
    '''
    每日平均销售价格和每日订单量关系图
    :param sku_info_dict:
    :param sku_name:
    :return:
    '''
    sku_info = get_sku_info(sku_info_dict,sku_name)
    day_number = sku_info['quantity-purchased']
    average_price = sku_info['price-amount'] / sku_info['quantity-purchased']
    average_price,day_number = average_price.to_frame(name=u'每日平均价'),day_number.to_frame(name=u'每日订单量')
    # print(average_price)
    data = pd.concat([average_price,day_number], axis=1)
    drawing(data, title=u'%s系列每日均价——订单量对比图' % sku_name,subplots=False)


def drawing(csv,title=u'数据分析',color = None,figsize = (6,6),linewidth = 1.5,alpha = 0.8,subplots=False):
    '''
    将数据在图上绘制（title命名不要加“/”等特殊字符）
    :param csv:
    :return:
    '''
    # 设置中文字体
    matplotlib.rc('font', **{'family': 'SimHei'})
    # 自定义颜色
    # if type(csv) == list:
    #     plt.plot(csv[u'YSW5402系列'], 'g-', csv[u'YSW1623系列'], 'r-')
    csv.plot(subplots=subplots,color = color,linewidth = linewidth , linestyle = '-' , title = title, alpha = alpha,rot=0,
             figsize = figsize,fontsize = 7,grid=True)

    # 自动化最佳比例
    plt.autoscale(tight=True)
    plt.legend(loc='best')
    # 定义坐标轴名称
    plt.xlabel(u'2018/2/12 - 2018/2/26')
    plt.ylabel(u'订单量(个)')
    if type(csv) == list:
        plt.savefig('%s.jpg' % title)
    elif type(csv) == type(pd.DataFrame()):
        plt.savefig('%s.jpg' % title)
    plt.show()


if __name__ == '__main__':
    filename = '0211-0225bak.csv'
    csv = get_csv(filename)
    # csv_day_order = get_day_order(csv)
    sku_info_dict = get_sku_info_dict(csv,['YSW5402','YSW1623','YSK37509','YSW1610','YSW7603','YSW8004','YSW27617'])
    # get_sku_info(sku_info_dict,'YSW5402')
    get_diagram_day_sku_list(sku_info_dict,['YSW5402','YSW1623','YSK37509'])
    get_average_price_quantity_purchased(sku_info_dict,'YSW1610')


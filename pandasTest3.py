# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd


def main():

    s = pd.Series([i*2 for i in range(1,11)])
    print(type(s))
    dates = pd.date_range('20170301',periods=8)
    df = pd.DataFrame(np.random.randn(8,5),index=dates,columns=list('ABCDE'))
    print(df)
    print('------------------------     Basic 操作   ----------------------------')
    # Basic 操作
    print(df.head(3))       # 打印前三行
    print(df.tail(2))       # 打印后两行
    print(df.index)         # 取索引
    print(df.values)        # 取值
    print(df.T)             # 行列互换
    print(df.sort_values('C',ascending=False))   # 根据C列排序,ascending=False升序降序
    print(df.sort_index(axis = 1,ascending=False))  # 根据属性值排序，降序处理
    print(df.describe())    # 打印每列的各种属性：count数量，mean平均值,std标准偏差,

    print('------------------------     Select   ----------------------------')
    # 选择
    print(df['A'])                      # 属性值选择
    # print(df['A':'C'])                # 属性值切片是没有的
    print(df[:3])
    # print(df['20170301'])             # index选择也是没有的
    print(df['20170301':'20170304'])    # index切片
    print(df.loc[dates[0]])             # index选择在这里
    print(df.loc['20170301':'20170304',['B','D']])             # 区间选择
    print(df.at[dates[0],'C'])          # 选择单独的值

    print(df.iloc[1:3,2:4])             # 区间选择
    print(df.iloc[1,4])                 # 选择第一行第四个数字
    print(df.iat[1,4])                  # 选择第一行第四个数字

    print(df[df.B > 0][df.A < 0])       # 条件选择
    print(df[df >0])                    # 返回大于0的数，小于0的返回NaN
    print(df[df['E'].isin([-10,10])])     # 类似sql 中的 in，不会用

    print('------------------------     Set   ----------------------------')
    # Set
    s1 = pd.Series(list(range(10,18)),index = pd.date_range('20170301',periods=8))
    df['F'] = s1                        # 添加新数据
    print(df)
    df.at[dates[0],'A'] = 0             # 修改数据
    print(df)
    df.iat[1,1] = 1
    df.loc[:,'D'] = np.array([4] * len(df))
    print(df)

    df2 = df.copy()
    df2[df2 > 0] = -df2                 # 将所有大于0的值变成负数
    print(df2)

    print('-------Test3 缺失值处理--------')
    df1 = df.reindex(index = dates[:4], columns = list('ABCD') + ["G"])
    df1.loc[dates[0]:dates[1],'G'] = 1
    print(df1)
    print(df1.dropna())                 # 丢弃处理
    print(df1.fillna(value=100))          # 填充处理



if __name__ == '__main__':
    main()
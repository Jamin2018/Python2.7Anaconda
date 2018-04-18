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
    print ('|||'*100)
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



    print('-------Test4 表统计与整合--------')
    print(df.mean())                    # 平均值
    print(df.var())                     # 平方差

    s = pd.Series([1,2,4,np.nan,5,7,9,7], index=dates)
    print(s)
    print(s.shift(2))                   # 值从上往下一定2格
    print(s.diff())                     # 获得该值减去Y轴上一个值获得的新值
    print(s.value_counts())             # 数字出现次数统计

    print(df)
    print(df.apply(np.cumsum))          # 累加值
    print(df.apply(lambda x:x.max() - x.min()))         # 极差

    # 整合
    pieces = [df[:3],df[-3:]]
    print(pd.concat(pieces))            # 拼接

    left = pd.DataFrame({'key':['x','y'],'value':[1,2]})
    right = pd.DataFrame({'key':['x','z'],'value':[3,4]})
    print(left)
    print(right)
    print('-------------')
    print(pd.merge(left,right,on='key' , how='left'))       # 以 key为主数据，以left 为模板进行整合数据
    print(pd.merge(left,right,on='key' , how='inner'))       # 以 key为主数据，交集数据key,进行整合
    print(pd.merge(left,right,on='key' , how='outer'))       # 以 key为主数据，并集数据key,进行整合
    print('-------------')
    df3 = pd.DataFrame({'A':['a','b','c','b'],'B':list(range(4))})
    print(df3)

    print(df3.groupby('A').sum())                   # 将 A 列中，相同的值相加


    import datetime
    df4 = pd.DataFrame({'A':['one','one','two','three'] * 6 ,
                        'B': ['a', 'b', 'c'] * 8,
                        'C':['foo','foo','foo','bar','bar','bar'] * 4,
                        'D' : np.random.randn(24),
                        'E' : np.random.randn(24),
                        'F':[datetime.datetime(2017,i,1) for i in range(1,13)]+
                             [datetime.datetime(2017,i,15) for i in range(1,13)]
                        })
    print(df4)
    print(pd.pivot_table(df4, values= 'D' , index= ['A','B'], columns= ['C']))      # 没搞懂



    print('-------Test5 时间、绘图、文件操作--------')

    # 时间序列
    t_exam = pd.date_range('20170301',periods=10,freq='S')
    print(t_exam)

    # 绘图功能
    ts = pd.Series(np.random.randn(1000) , index=pd.date_range('20170301',periods=1000))

    ts = ts.cumsum()
    print('''绘图''')
    print(ts)
    # 导入绘图功能
    from pylab import *
    ts.plot()
    show()


    # 文件操作

    # CSV读入
    df6 = pd.read_csv('./0211-0225bak.csv')
    df6.to_csv('./text_csv.csv')
    # print(df6)

    # excel读入
    df7 = pd.read_excel('./sku.xlsx','Sheet1')
    df7.to_excel('./text_excel.xlsx')
    # print(df7)


if __name__ == '__main__':
    main()
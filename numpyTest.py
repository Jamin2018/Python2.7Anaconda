# -*- coding: utf-8 -*-

import numpy as np

def main():
    lst = [[1,3,5],[2,4,6]]
    print(type(list))
    np_lst = np.array(lst)
    print(type(np_lst))

    np_lst = np.array(lst,dtype=np.float)
    # dtype数据类型有：
    #bool,int,int8,int16,int32...unit8,unit16,...,float,float16...,complex64..

    print(np_lst.shape) # 指明形状：2行3列
    print(np_lst.ndim)  # 指明数组维度：2
    print(np_lst.dtype) # 数据类型
    print(np_lst.itemsize)  # 64位占8个字节
    print(np_lst.size)  # 长度
    print('-------------------------------------------------------')
    #2 Some Arrays
    print(np.zeros([2,4]))      # 数组初始化,基数为0
    print(np.ones([3,5]))       # 数组初始化,基数为1
    print('-----Rand------')
    print(np.random.rand())     # 随机0到1之间的数
    print(np.random.rand(2,4))  # 生成2行4列的随机0-1之间的数
    print('-----Randint------')
    print(np.random.randint(1,10,4))    # 生成随机整数，第三个参数为个数
    print('-----Randn------')
    print(np.random.randn(2,4))     # 生成正态分布的随机数（-1~1）之间
    print('-----Choice------')
    print(np.random.choice([10,20,30])) # 随机选数
    print('-----Distribute------')
    print(np.random.beta(1,10,100))     # beta分布

    print('-------------------------------------------------------')
    # 2  Arrays Opes
    print(np.arange(1,11))
    print(np.arange(1,11)).reshape([2,5])
    lst = np.arange(1,11).reshape([2,-1])

    print(np.exp(lst))
    print(np.exp2(lst))
    print(np.sqrt(lst))
    print(np.sin(lst))
    print(np.log(lst))
    print('-----Sum------')
    print(lst.sum())
    print(lst.sum(axis=0))
    print(lst.sum(axis=1))
    print('-----Min------')
    print(lst.min())
    print(lst.min(axis=0))
    print(lst.min(axis=1))
    print('-----Max------')
    print(lst.max())
    print(lst.max(axis=0))
    print(lst.max(axis=1))


if __name__ == '__main__':
    main()
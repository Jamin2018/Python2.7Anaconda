# -*- coding: utf-8 -*-

import numpy as np

def main():
    import matplotlib.pyplot as plt
    # 绘制线
    x = np.linspace(-np.pi,np.pi,256,endpoint=True)    # endpoint=True 是否包含最后一个点
    c,s = np.cos(x),np.sin(x)

    plt.figure(1)
    # x自变量，c因变量
    plt.plot(x,c,color = 'green' , linewidth = 1.0 , linestyle = '-' , label = 'COS', alpha = 0.5)
    plt.plot(x,s,label = 'SIN')           # x自变量，s因变量
    plt.title('COS-SIN')   # 名字

    ax = plt.gca()          # 轴编辑器
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_position(('data',0))
    ax.spines['bottom'].set_position(('data',0))
    plt.show()

if __name__ == '__main__':
    main()
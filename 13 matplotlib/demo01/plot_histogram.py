# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :   2021/5/31 15:48
# @Author    :   Chasion
# Description:
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator
import matplotlib
import os
import pandas as pd
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False


def plot(path):
    names = os.listdir(path)
    # print(names)
    xx = []
    yy = []
    for i in range(len(names)):
        address = path + r'\\' + names[i]
        data = pd.read_csv(address).values
        x = data[:, 0]
        y = data[:, 1]
        xx.append(x)
        yy.append(y)

    plt.xlim(0, 1)
    plt.ylim(0, 400)
    # print(xx[3])
    # print(yy[3])
    labels_list = ['fBm3:Ana', 'fBm3:LB', 'fBm2:Ana', 'fBm2:LB']
    color_list = ['grey', 'sandybrown', 'b', 'skyblue']
    line_list = ['-', '--', '-.', ':']
    marker_list = ['o', '^', 's', 'D']
    x_tickes = ['1e-06', '1e-05', '1e-04', '1e-03', '1e-02', '1e-01', '1']
    for i in range(len(xx)):
        plt.plot(yy[i], xx[i], color=color_list[i], linestyle=line_list[i], marker=marker_list[i], label=labels_list[i])
    plt.xlabel('溢出概率(△)', fontsize=14)
    plt.ylabel('缓存大小(b)', fontsize=14)
    plt.xticks([0, 0.167, 0.167 * 2, 0.167 * 3, 0.167 * 4, 0.167 * 5, 1.0], x_tickes)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    path = 'datasets\p1'
    plot(path)

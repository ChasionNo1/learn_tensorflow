# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :   2021/7/30 14:53
# @Author    :   Chasion
# Description:
import matplotlib
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
# matplotlib.rcParams['axes.unicode_minus'] = False
from matplotlib import rcParams
config = {
    "font.family":'Times New Roman',  # 设置字体类型
    # "font.size": 80,
#   "mathtext.fontset":'stix',
}
rcParams.update(config)


def plot(path):
    data = pd.read_excel(path, header=None).values
    # print(data)
    labels_list = ['MMPP1:Analysis', 'MMPP1:Simulation', 'fBm2:Analysis', 'fBm2:Simulation', 'fBm3:Analysis', 'fBm3:Simulation', 'fBm4:Analysis', 'fBm4:Simulation']
    color_list = ['#CD5C5C', '#F15C80', '#FF7F50', '#FFA500', '#3398DB', '#7CB5EC', '#3CB371', '#40E0D0']
    x_tickes = ['1e-06', '1e-05', '1e-04', '1e-03', '1e-02', '1e-01']
    size = 6
    x = np.arange(size)
    total_width, n = 0.8, 8
    width = total_width / n
    x = x - (total_width - width) / 2
    for i in range(8):
        plt.bar(x + i * width, data[i], width=width, color=color_list[i], label=labels_list[i])

    plt.xticks([0, 1, 2, 3, 4, 5], x_tickes)
    plt.xlabel('maximum overflow probability', fontsize=14)
    plt.ylabel('minimum buffer size', fontsize=14)
    plt.legend()
    plt.savefig('./datasets/picture/fig2.png', dpi=800)
    plt.show()


if __name__ == '__main__':
    path = './datasets/new_fig/fig2.xlsx'
    plot(path)
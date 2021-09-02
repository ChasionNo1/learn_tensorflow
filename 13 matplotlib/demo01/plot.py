import matplotlib.pyplot as plt
import pandas as pd
import os
import matplotlib
import numpy as np

# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
# matplotlib.rcParams['axes.unicode_minus'] = False


def plot(path):
    names = os.listdir(path)
    # print(names)
    xx = []
    for i in range(len(names)):
        address = path + r'\\' + names[i]
        data = pd.read_csv(address, header=None).values
        x = data[:, 0][::-1]
        xx.append(x)

    data5 = np.random.random(7)
    data6 = np.random.random(7)
    xx.append(data5)
    xx.append(data6)
    # plt.xlim(0, 1)
    plt.ylim(0, 3000)
    # print(xx[3])
    # print(yy[3])
    labels_list = ['MMPP1:Analysis', 'MMPP1:Simulation', 'fBm2:Analysis', 'fBm2:Simulation', 'fBm3:Analysis', 'fBm3:Simulation']
    # labels_list = ['fBm2:Analysis', 'fBm2:Simulation', 'fBm3:Analysis', 'fBm3:Simulation']
    color_list = ['#0062AB', '#009BD4', '#039947', '#82B943', '#E65800', '#E18800']
    line_list = ['-', '--', '-.', ':']
    marker_list = ['o', '^', 's', 'D']
    x_tickes = ['1e-06', '1e-05', '1e-04', '1e-03', '1e-02', '1e-01', '1']
    size = 7
    x = np.arange(size)
    total_width, n = 0.8, 6
    width = total_width/n
    x = x - (total_width - width) / 2
    plt.bar(x, xx[4], width=width, color=color_list[0], label=labels_list[0])
    plt.bar(x + width, xx[5], width=width, color=color_list[1], label=labels_list[1])
    plt.bar(x + 2 * width, xx[0], width=width, color=color_list[2], label=labels_list[2])
    plt.bar(x + 3 * width, xx[1], width=width, color=color_list[3], label=labels_list[3])
    plt.bar(x + 4 * width, xx[2], width=width, color=color_list[4], label=labels_list[4])
    plt.bar(x + 5 * width, xx[3], width=width, color=color_list[5], label=labels_list[5])
    # for i in range(len(xx)):
    #     plt.plot(yy[i], xx[i], color=color_list[i], linestyle=line_list[i], marker=marker_list[i], label=labels_list[i])
    plt.xlabel('maximum overflow probability', fontsize=14)
    plt.ylabel('minimum buffer size', fontsize=14)
    plt.xticks([0, 1, 2, 3, 4, 5, 6], x_tickes)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    path = 'datasets\p2'
    plot(path)
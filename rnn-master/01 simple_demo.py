"""
文件说明
简单循环神经网路前向传播过程
"""
import numpy as np

# 定义相关参数，ini_state是输入到t1的t0时刻输出的状态
# 输入数据
x = [0.8, 0.1]
# t0时刻的h值
init_state = [0.3,  0.6]
# 相邻时刻隐藏单元间的权重矩阵
w = np.asarray([[0.2, 0.4], [0.7, 0.3]])
# 输入的权重
u = np.asarray([0.8, 0.1])
# 偏置
b_h = np.asarray([0.2, 0.1])
# 输出权重矩阵
v = np.asarray([[0.5], [0.5]])
# 输出偏置
b_o = 0.1

# 执行两轮循环，模拟前向传播过程
'''
ht = tanh(b_h + w * h_t-1 + u * x_t)
'''
for i in range(len(x)):
    # 每次输入一个时间点的数据，获取总长度，得到需要计算的次数
    # numpy的dot函数用于矩阵相乘，函数原型为dot(a, b, out)
    before_activation = np.dot(init_state, w) + x[i] * u + b_h

    # numpy也提供了tanh函数，用于实现双曲正切函数的计算
    state = np.tanh(before_activation)

    # 本时刻的状态作为下一时刻的初始状态
    init_state = state

    # 计算本时刻的输出
    final_output = np.dot(state, v) + b_o

    # 打印t1和t2时刻的状态和输出信息
    print('t%s state: %s' % (i + 1, state))
    print('t%s output: %s' % (i + 1, final_output))



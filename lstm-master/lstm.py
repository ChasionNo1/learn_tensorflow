import random

import numpy as np
import math


# 定义激活函数，sigmoid和tanh
# simgoid = 1 / ( 1 + e^(-x))
# tanh = (e^(x)-e^(-x))/(e^x + e^(-x))
def sigmoid(x): 
    return 1. / (1 + np.exp(-x))


# simgoid的导数
def sigmoid_derivative(values): 
    return values*(1-values)


# tanh的导数
def tanh_derivative(values): 
    return 1. - values ** 2


# createst uniform random array w/ values in [a,b) and shape args
# np.random.seed(0):设置随机数生成的种子
# np.random.rand(*args):*args是生成随机数的形状（维数），生成的数组元素乘以（b-a）+a
def rand_arr(a, b, *args): 
    np.random.seed(0)
    return np.random.rand(*args) * (b - a) + a


# 定义lstm参数类
class LstmParam:
    def __init__(self, mem_cell_ct, x_dim):
        # men_cell_ct: cell_state的维度？ 这里像是ht的维度
        # x_dim: 输入数据的维度
        self.mem_cell_ct = mem_cell_ct
        self.x_dim = x_dim
        # 连接的长度
        # [ h(t-1)
        #    xt]
        concat_len = x_dim + mem_cell_ct
        # weight matrices
        # 各个矩阵的大小，列数等于x和h拼接后的行数，行数和ct相同
        # 四个门控权重矩阵，f遗忘门，i信息门，o输出门，g输入门
        self.wg = rand_arr(-0.1, 0.1, mem_cell_ct, concat_len)
        self.wi = rand_arr(-0.1, 0.1, mem_cell_ct, concat_len) 
        self.wf = rand_arr(-0.1, 0.1, mem_cell_ct, concat_len)
        self.wo = rand_arr(-0.1, 0.1, mem_cell_ct, concat_len)
        # bias terms
        self.bg = rand_arr(-0.1, 0.1, mem_cell_ct) 
        self.bi = rand_arr(-0.1, 0.1, mem_cell_ct) 
        self.bf = rand_arr(-0.1, 0.1, mem_cell_ct) 
        self.bo = rand_arr(-0.1, 0.1, mem_cell_ct) 
        # diffs (derivative of loss function w.r.t. all parameters)
        # 损失函数的导数，所有参数，用于梯度下降
        self.wg_diff = np.zeros((mem_cell_ct, concat_len)) 
        self.wi_diff = np.zeros((mem_cell_ct, concat_len)) 
        self.wf_diff = np.zeros((mem_cell_ct, concat_len)) 
        self.wo_diff = np.zeros((mem_cell_ct, concat_len)) 
        self.bg_diff = np.zeros(mem_cell_ct) 
        self.bi_diff = np.zeros(mem_cell_ct) 
        self.bf_diff = np.zeros(mem_cell_ct) 
        self.bo_diff = np.zeros(mem_cell_ct) 

    def apply_diff(self, lr = 1):
        # 梯度下降，求出梯度值，然后沿着这个方向下降（减去一个数值）
        # 又将下降所有参数重置为0矩阵
        self.wg -= lr * self.wg_diff
        self.wi -= lr * self.wi_diff
        self.wf -= lr * self.wf_diff
        self.wo -= lr * self.wo_diff
        self.bg -= lr * self.bg_diff
        self.bi -= lr * self.bi_diff
        self.bf -= lr * self.bf_diff
        self.bo -= lr * self.bo_diff
        # reset diffs to zero
        self.wg_diff = np.zeros_like(self.wg)
        self.wi_diff = np.zeros_like(self.wi) 
        self.wf_diff = np.zeros_like(self.wf) 
        self.wo_diff = np.zeros_like(self.wo) 
        self.bg_diff = np.zeros_like(self.bg)
        self.bi_diff = np.zeros_like(self.bi) 
        self.bf_diff = np.zeros_like(self.bf) 
        self.bo_diff = np.zeros_like(self.bo) 


class LstmState:
    def __init__(self, mem_cell_ct, x_dim):
        # 这里初始化矩阵为一维向量,向量长度为men_cell_ct
        # 可以理解为state,也就是经过判断后的结果(列向量？)
        # g i f o
        self.g = np.zeros(mem_cell_ct)
        self.i = np.zeros(mem_cell_ct)
        self.f = np.zeros(mem_cell_ct)
        self.o = np.zeros(mem_cell_ct)
        # s h 是什么?  s 是 cell state, h: hidden state
        self.s = np.zeros(mem_cell_ct)
        self.h = np.zeros(mem_cell_ct)
        self.bottom_diff_h = np.zeros_like(self.h)
        self.bottom_diff_s = np.zeros_like(self.s)


class LstmNode:
    # 初始化，底部数据，计算梯度
    def __init__(self, lstm_param, lstm_state):
        # store reference to parameters and to activations
        # 存储对参数和激活的引用
        self.state = lstm_state
        self.param = lstm_param
        # non-recurrent input concatenated with recurrent input
        # 非递归输入与递归输入连接
        self.xc = None

    def bottom_data_is(self, x, s_prev=None, h_prev=None):
        # if this is the first lstm node in the network
        if s_prev is None: s_prev = np.zeros_like(self.state.s)
        if h_prev is None: h_prev = np.zeros_like(self.state.h)
        # save data for use in backprop
        self.s_prev = s_prev
        self.h_prev = h_prev

        # concatenate x(t) and h(t-1)
        # 连接x和h
        # x 是 seed（0）的一组随机数，数量是50
        # h_prev是零向量，大小是100
        xc = np.hstack((x,  h_prev))
        print('xc:', xc.shape)
        # 在水平方向上平铺, 要求维度一致
        '''
        [[1 4 5]
         [2 9 3]]
        [[6 0 1]
         [2 3 6]]
        [[1 4 5 6 0 1]
         [2 9 3 2 3 6]]
        '''

        '''
        开始计算:
        
        遗忘门:
        f = sigmoid(wf*xc+bf)
        
        信息更新门:
        i = sigmoid(wi*xc+bi)
        输入数据,将结果转换成-1到1之间的值
        g = tanh(w*xc + bg)
        
        更新细胞状态:
        新细胞状态 = 旧细胞状态 * 遗忘门结果 + 更新信息内容
        s = s_prev * f + i * g
        
        输出:
        o = sigmoid(wo*xc+bo)
        h = o * tanh(s)
        '''
        print('wg:', self.param.wg.shape)
        self.state.g = np.tanh(np.dot(self.param.wg, xc) + self.param.bg)
        # print('state.g:', self.state.g.shape)
        self.state.i = sigmoid(np.dot(self.param.wi, xc) + self.param.bi)
        self.state.f = sigmoid(np.dot(self.param.wf, xc) + self.param.bf)
        self.state.o = sigmoid(np.dot(self.param.wo, xc) + self.param.bo)
        self.state.s = self.state.g * self.state.i + s_prev * self.state.f
        # 这里是不是缺少一个tanh(self.state.s) ????
        # 这里没有设置一个ht和输出的yt，所以ht就是预测值了
        self.state.h = np.tanh(self.state.s) * self.state.o
        # 保存拼接后的结果
        self.xc = xc

    # 计算梯度部分
    def top_diff_is(self, top_diff_h, top_diff_s):
        # notice that top_diff_s is carried along the constant error carousel: top_diff_s沿着恒定误差轮播传送
        # 求导开始
        '''

        :param top_diff_h: dL(t)/dh(t) = dl(t)/dh(t) + dL(t+1)/dh(t)
        :param top_diff_s: dL(t+1)/ds(t)

        s = s_prev * f + i * g
        self.state.h = self.state.s * self.state.o
        h = s * o  ->  dh = ods + sdo , sdo = 0? --> dh/ds = o

        ds 是 dL/ds = (dL(t)/dhi(t)) * (dhi(t)/dsi(t) + dL(t+1)/dsi(t)
        '''
        ds = self.state.o * top_diff_h + top_diff_s
        do = self.state.s * top_diff_h
        di = self.state.g * ds
        dg = self.state.i * ds
        df = self.s_prev * ds

        # diffs w.r.t. vector inside sigma / tanh function
        # diffs（微分） 关于向量
        # 这里是有疑问的，按理说这个self.state.i应该是通过激活函数后的，可这里却是没有通过激活函数
        # it = sigmoid(it~)
        # di_input = dl/dit~ = (dl/dit) * (dit/dit~)
        # 这样就解释的通，可是在之前的定义的时候明明是加了sigmoid的
        # 猜测，不是同一个参数，这里加了self
        di_input = sigmoid_derivative(self.state.i) * di 
        df_input = sigmoid_derivative(self.state.f) * df
        do_input = sigmoid_derivative(self.state.o) * do 
        dg_input = tanh_derivative(self.state.g) * dg

        # diffs w.r.t. inputs
        # w参数和b偏置的微分
        # it~ = wi * xc + bi
        # dL/dit~ = dL/d(wi * xc) = (1/xc) * (dL/dwi)
        self.param.wi_diff += np.outer(di_input, self.xc)
        self.param.wf_diff += np.outer(df_input, self.xc)
        self.param.wo_diff += np.outer(do_input, self.xc)
        self.param.wg_diff += np.outer(dg_input, self.xc)
        self.param.bi_diff += di_input
        self.param.bf_diff += df_input       
        self.param.bo_diff += do_input
        self.param.bg_diff += dg_input       

        # compute bottom diff
        # 计算底部的微分，输入 xc  ->  dxc
        # 因为有四个门输入，叠加起来即可，
        dxc = np.zeros_like(self.xc)
        # .T是矩阵转置np的函数
        dxc += np.dot(self.param.wi.T, di_input)
        dxc += np.dot(self.param.wf.T, df_input)
        dxc += np.dot(self.param.wo.T, do_input)
        dxc += np.dot(self.param.wg.T, dg_input)

        # save bottom diffs
        self.state.bottom_diff_s = ds * self.state.f
        self.state.bottom_diff_h = dxc[self.param.x_dim:]


class LstmNetwork():
    # lstm网络的搭建
    # 初始化参数，节点列表，输入队列
    def __init__(self, lstm_param):
        self.lstm_param = lstm_param
        self.lstm_node_list = []
        # input sequence
        self.x_list = []

    def y_list_is(self, y_list, loss_layer):
        """
        Updates diffs by setting target sequence 
        with corresponding loss layer. 
        Will *NOT* update parameters.  To update parameters,
        call self.lstm_param.apply_diff()
        通过设置具有相应损失层的目标序列来更新差异。
        """
        # 断言 输入队列长度和标签队列长度一致
        assert len(y_list) == len(self.x_list)
        # index = 输入队列 - 1， 假设长度为4，那么index = 3， 而y_list[index] = y_list[3] 是最后一个元素
        idx = len(self.x_list) - 1
        # first node only gets diffs from label ...
        loss = loss_layer.loss(self.lstm_node_list[idx].state.h, y_list[idx])
        # print(self.lstm_node_list[idx].state.h)
        # loss的参数为hi[t] 和 标签y
        diff_h = loss_layer.bottom_diff(self.lstm_node_list[idx].state.h, y_list[idx])
        # here s is not affecting loss due to h(t+1), hence we set equal to zero
        diff_s = np.zeros(self.lstm_param.mem_cell_ct)
        self.lstm_node_list[idx].top_diff_is(diff_h, diff_s)
        idx -= 1

        ### ... following nodes also get diffs from next nodes, hence we add diffs to diff_h
        ### we also propagate error along constant error carousel using diff_s
        while idx >= 0:
            loss += loss_layer.loss(self.lstm_node_list[idx].state.h, y_list[idx])
            diff_h = loss_layer.bottom_diff(self.lstm_node_list[idx].state.h, y_list[idx])
            diff_h += self.lstm_node_list[idx + 1].state.bottom_diff_h
            diff_s = self.lstm_node_list[idx + 1].state.bottom_diff_s
            self.lstm_node_list[idx].top_diff_is(diff_h, diff_s)
            idx -= 1 

        return loss

    def x_list_clear(self):
        self.x_list = []

    def x_list_add(self, x):
        # 参数传入的是array随机数组
        self.x_list.append(x)
        # 第一次的时候list_node_list还是空列表
        if len(self.x_list) > len(self.lstm_node_list):
            # need to add new lstm node, create new state mem
            # g,i,f,o门状态，大小为100的零向量->[0,0,.....0]
            lstm_state = LstmState(self.lstm_param.mem_cell_ct, self.lstm_param.x_dim)
            # 这部分进行了，初始化，底部数据，计算梯度
            self.lstm_node_list.append(LstmNode(self.lstm_param, lstm_state))
            '''
            lstm_node_list是节点对象，里面有节点的基本信息
            [<lstm.LstmNode object at 0x000001E352E0AB88>, <lstm.LstmNode object at 0x000001E352D8F448>, 
            <lstm.LstmNode object at 0x000001E352D8F548>, <lstm.LstmNode object at 0x000001E352D8F5C8>]
            '''
            # print(self.lstm_node_list)

        # get index of most recent x input
        idx = len(self.x_list) - 1
        if idx == 0:
            # 如果x_list = 1 ，那么idx = 0，此时就列表就一个元素，并将array作为bottom_data
            # no recurrent inputs yet
            self.lstm_node_list[idx].bottom_data_is(x)
        else:
            # 如果x不是第一个输入的，假设idx = 1，s_prev和h_prev是s(t-1)和h(t-1)上一时刻的状态
            s_prev = self.lstm_node_list[idx - 1].state.s
            h_prev = self.lstm_node_list[idx - 1].state.h
            self.lstm_node_list[idx].bottom_data_is(x, s_prev, h_prev)


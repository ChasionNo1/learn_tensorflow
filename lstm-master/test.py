import numpy as np

from lstm import LstmParam, LstmNetwork


class ToyLossLayer:
    """
    Computes square loss with first element of hidden layer array.
    """
    @classmethod
    def loss(self, pred, label):
        # h是输出的预测值是一个大小为100的向量，为什么只取了第一个值来计算？
        '''
        By running `python test.py` you will have a minimal example of an lstm network learning to
        predict an output sequence of numbers in [-1,1] by using a Euclidean loss on the first element of each node's hidden layer.
        '''
        return (pred[0] - label) ** 2

    @classmethod
    def bottom_diff(self, pred, label):
        # predict预测值和标签值
        # 定义0矩阵，矩阵大小和hi(t)一样
        diff = np.zeros_like(pred)
        # 第一个元素 = 平方损失的导数
        diff[0] = 2 * (pred[0] - label)
        return diff


def example_0():
    # learns to repeat simple sequence from random inputs
    np.random.seed(0)

    # parameters for input data dimension and lstm cell count M
    mem_cell_ct = 100
    x_dim = 50
    lstm_param = LstmParam(mem_cell_ct, x_dim)
    lstm_net = LstmNetwork(lstm_param)
    y_list = [-0.5, 0.2, 0.1, -0.5]
    # 这行代码的意思是，生成一个array列表，array是大小为50的随机数组成，列表的长度有y_list的大小决定
    # 所以生成了四个array
    input_val_arr = [np.random.random(x_dim) for _ in y_list]
    # 设置学习的次数为200
    for cur_iter in range(200):
        print("iter", "%2s" % str(cur_iter), end=": ")
        for ind in range(len(y_list)):
            # 这部分将生成的array添加到lstm_net中，调用了x_list_add函数
            lstm_net.x_list_add(input_val_arr[ind])

        print("y_pred = [" +
              ", ".join(["% 2.5f" % lstm_net.lstm_node_list[ind].state.h[0] for ind in range(len(y_list))]) +
              "]", end=", ")

        loss = lstm_net.y_list_is(y_list, ToyLossLayer)
        print("loss:", "%.3e" % loss)
        lstm_param.apply_diff(lr=0.1)
        lstm_net.x_list_clear()


if __name__ == "__main__":
    example_0()


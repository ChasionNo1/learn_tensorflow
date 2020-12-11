"""
全连接层的每一个结点都与上一层的所有结点相连，用来把前边提取到的特征综合起来。由于其全相连的特性，一般全连接层的参数也是最多的。

"""
import tensorflow as tf

batch_size = 12


def fc(inp, num_out, name, relu=True):
    with tf.variable_scope(name):
        # 得到输入数据的维数
        # 池化层的输出结果是什么样的？
        # 3*3*64 特征图的大小和个数
        inp_reshape = tf.reshape(inp, [batch_size, -1])
        dim = inp_reshape.get_shape()[1].value
        w = tf.Variable(tf.random_normal([dim, num_out]), name='weights')
        b = tf.Variable(tf.constant(0.1, [num_out]), name='biases')
        return tf.nn.relu(tf.matmul(inp_reshape, w) + b)




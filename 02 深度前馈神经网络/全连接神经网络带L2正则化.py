"""
文件说明
计算一个3层全连接神经网络带L2正则化损失函数

1、设置超参
2、初始化输入数据和标签
3、定义网络结构
4、初始化可学习参数：w、b
5、计算输出
6、计算损失、进行正则化
7、训练
"""
import tensorflow as tf
import numpy as np


# 定义训练轮数
training_steps = 30000


# 2、初始化输入数据和标签

data = []
label = []
for i in range(200):
    # 平均分布生成x1,x2
    x1 = np.random.uniform(-1, 1)
    x2 = np.random.uniform(0, 2)
    # (x1,x2)如果在单位圆内，则标签为0，反之
    if x1**2 + x2**2 <= 1:
        data.append([np.random.normal(x1, 0.1), np.random.normal(x2, 0.1)])
        label.append(0)
    else:
        data.append([np.random.normal(x1, 0.1), np.random.normal(x2, 0.1)])
        label.append(1)
# 将生成的列表变成numpy数据格式（张量）
data = np.hstack(data).reshape(-1, 2)
label = np.hstack(label).reshape(-1, 1)


# 3、定义网络结构
def layer(input_tensor, w1, b1, w2, b2, w3, b3):
    l1 = tf.nn.relu(tf.matmul(input_tensor, w1) + b1)
    l2 = tf.nn.relu(tf.matmul(l1, w2) + b2)
    l3 = tf.matmul(l2, w3) + b3
    return l3


# # 4、初始化可学习参数：w、b
# def set_param():
#     # 三层的网络结构共有6个参数,权重矩阵采用随机数，偏置是常数
#     # 如何确定各个参数的大小？ input:200x2, w1:2x10(相当于10组滤波器对input的两百行数据做一个特征提取，后面再加上一个偏置）
#     # l1输出的大小为200x10，作为l2的输入,
#     # 最终的输出应该是200x0
#
#     return w1, b1, w2, b2, w3, b3
w1 = tf.Variable(tf.compat.v1.truncated_normal([2, 10], stddev=0.1))
b1 = tf.Variable(tf.compat.v1.constant(0.1, shape=[10]))
w2 = tf.Variable(tf.compat.v1.truncated_normal([10, 10], stddev=0.1))
b2 = tf.Variable(tf.compat.v1.constant(0.1, shape=[10]))
w3 = tf.Variable(tf.compat.v1.truncated_normal([10, 1], stddev=0.1))
b3 = tf.Variable(tf.compat.v1.constant(0.1, shape=[1]))


# 5、计算输出
# 6、计算损失、进行正则化

x = tf.compat.v1.placeholder(dtype=tf.float32, shape=[None, 2], name='x-input')
y_ = tf.compat.v1.placeholder(dtype=tf.float32, shape=[None, 1], name='y_')
y = layer(x, w1, b1, w2, b2, w3, b3)
# 计算平方差损失
error_loss = tf.reduce_sum(tf.pow(y_ - y, 2)) / len(data)
tf.add_to_collection('losses', error_loss)
# 正则化,在新版中已经被删掉了，选择tf.keras.regularizers.l2(0.005)来代替
regularizer = tf.keras.regularizers.l2(0.005)
regularizetion = regularizer(w1) + regularizer(w2) + regularizer(w3)

tf.add_to_collection('losses', regularizetion)
losses = tf.add_n(tf.get_collection('losses'))
train_op = tf.compat.v1.train.AdamOptimizer(0.01).minimize(losses)
with tf.compat.v1.Session() as sess:
    # 所有变量必须初始化后才能使用，不要忘记run()运行初始化
    tf.compat.v1.global_variables_initializer().run()
    for i in range(training_steps):
        sess.run(train_op, feed_dict={x: data, y_: label})
        if i % 2000 == 0:
            loss_value = sess.run(losses, feed_dict={x: data, y_: label})
            print(i, loss_value)





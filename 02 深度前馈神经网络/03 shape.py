"""
文件说明

"""
import numpy as np
import tensorflow as tf


x1 = tf.compat.v1.random_normal(shape=[200, 2], stddev=0.1)
# data = np.hstack().reshape(-1, 2)
# print(data)
w1 = tf.compat.v1.Variable(tf.random.truncated_normal([2, 10], stddev=0.1))
# 矩阵的乘法
y1 = tf.compat.v1.matmul(x1, w1)
with tf.compat.v1.Session() as sess:
    # Tensorflow中，所有变量都必须初始化才能使用。
    tf.compat.v1.global_variables_initializer().run()
    print(sess.run(w1))
    print(sess.run(y1))
    print(y1.shape)

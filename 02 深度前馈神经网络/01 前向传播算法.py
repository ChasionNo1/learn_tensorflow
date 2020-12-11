"""
文件说明
matmul(a,b,transpose_a,transpose_b,adjoint_a,adjoint_b,a_is_sparse,b_is_sparse,name)
参数：
transpose_a,transpose_b,adjoint_a,adjoint_b,a_is_sparse,b_is_sparse:默认值为false，name默认值为none
a，b是传入矩阵，需要满足计算条件
"""
import tensorflow as tf
# 在参与矩阵运算时，需要通过shape来指定矩阵的形状
# 或者直接通过value来指明形状，[[0.9, 0.3]]
x = tf.compat.v1.constant([0.9, 0.85], shape=(1, 2))
# 创建权值变量
w1 = tf.compat.v1.Variable(tf.compat.v1.constant([[0.2, 0.1, 0.3], [0.2, 0.4, 0.3]], shape=(2, 3)), name="w1")
w2 = tf.compat.v1.Variable(tf.compat.v1.constant([0.2, 0.5, 0.25], shape=(3, 1)), name="w2")
# 创建偏置参数
b1 = tf.compat.v1.constant([-0.3, 0.1, 0.2], shape=(1, 3), name="b1")
b2 = tf.compat.v1.constant([-0.3], shape=(1, 1), name="b2")
# 初始化全部变量
init_op = tf.compat.v1.global_variables_initializer()
# 矩阵的点乘
a = tf.compat.v1.matmul(x, w1) + b1
y = tf.compat.v1.matmul(a, w2) + b2

with tf.compat.v1.Session() as sess:
    sess.run(init_op)
    # [[0.15625]]
    print(sess.run(y))

'''
权重参数初始化为一个随机矩阵，偏置参数初始化为全1，或者全0
'''
w1 = tf.compat.v1.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
w2 = tf.compat.v1.Variable(tf.random_normal([3, 1], stddev=1, seed=1))
b1 = tf.compat.v1.Variable(tf.compat.v1.zeros([1, 3]))
b2 = tf.compat.v1.Variable(tf.compat.v1.ones([1, 1]))

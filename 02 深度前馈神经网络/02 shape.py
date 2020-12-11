"""
文件说明

"""
import tensorflow as tf
# 当提供的元素个数大于要求的维度所需个数，报错
# Too many elements provided. Needed at most 3, but received 6

# 当提供的元素个数小于要求维度所需个数，将重复最后一个元素来填充
# [[1 2 3]
#  [2 3 4]
#  [4 4 4]]
x = tf.compat.v1.constant([[1, 2, 3], [2, 3, 4]], shape=(3, 3))
w1 = tf.Variable(tf.random.truncated_normal([2, 10], stddev=0.1))
with tf.compat.v1.Session() as sess:
    # Tensorflow中，所有变量都必须初始化才能使用。
    tf.global_variables_initializer().run()
    print(sess.run(x))
    print(sess.run(w1))
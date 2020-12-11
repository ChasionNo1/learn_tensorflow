"""
文件说明

"""
import tensorflow as tf

x = tf.compat.v1.constant([[1.0, 2.0]])
w1 = tf.compat.v1.Variable(tf.compat.v1.random_normal([2, 3], stddev=1, seed=1))
w2 = tf.compat.v1.Variable(tf.compat.v1.random_normal([3, 1], stddev=1, seed=1))
a = tf.compat.v1.matmul(x, w1)
y = tf.compat.v1.matmul(a, w2)
init_op = tf.compat.v1.initialize_all_variables()

with tf.compat.v1.Session() as sess:
    sess.run(init_op)
    # [[7.2020965]]
    print(sess.run(y))
    # [<tf.Variable 'Variable:0' shape=(2, 3) dtype=float32_ref>, <tf.Variable 'Variable_1:0' shape=(3, 1) dtype=float32_ref>]
    print(tf.global_variables())
    '''
    [array([[-0.8113182 ,  1.4845988 ,  0.06532937],
       [-2.4427042 ,  0.0992484 ,  0.5912243 ]], dtype=float32), array([[-0.8113182 ],
       [ 1.4845988 ],
       [ 0.06532937]], dtype=float32)]
    '''
    print(sess.run(tf.global_variables()))

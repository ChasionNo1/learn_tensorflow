"""
文件说明
placeholder机制：解决如何在有限的输入节点上实现高效地接收大量数据的问题
"""
import tensorflow as tf
# 用placeholder定义一个位置 placeholder(dtype,shape,name)
# dtype需要指定，不可以改变，shape维度可以不提供
a = tf.compat.v1.placeholder(tf.float32, shape=2, name="input")
b = tf.compat.v1.placeholder(tf.float32, shape=2, name="input")
result = a + b

with tf.compat.v1.Session() as sess:
    # run(self,fetches,feed_dict,options,run_metadata)
    # feed_dict是一个字典
    sess.run(result, feed_dict={a: [1.0, 2.0], b: [3.0, 4.0]})
    # Tensor("add:0", shape=(2,), dtype=float32)
    print(result)

"""
文件说明

"""
import tensorflow as tf

labels = [[0, 1, 0], [0, 1, 0], [1, 0, 0]]
logits = tf.constant(value=[[0.3, 0.3, 0.2], [0, 1, 0.5], [1, 1, 0]],
                     dtype=tf.float32, shape=[3, 3])

loss = tf.nn.softmax_cross_entropy_with_logits_v2(labels=labels, logits=logits)

with tf.Session() as sess:
    print(labels)
    print(sess.run(logits))
    print(sess.run(loss))
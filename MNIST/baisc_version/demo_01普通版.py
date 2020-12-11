"""
初始版本，加载数据，初始化，定义网络，输出，
"""
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

mnist = input_data.read_data_sets('../MNIST_data', one_hot=True)

x = tf.placeholder(tf.float32, [None, 784])
y_ = tf.placeholder(tf.float32, [None, 10])
w = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.matmul(x, w) + b

# 交叉熵损失
cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.argmax(y_, 1))
train_op = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
# tf.argmax返回最大数的坐标索引，tf.equal返回两个是否相等的布尔值
# 这里的预测解释：第一个是网络输出，第二个是标签值
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
# tf.cast:数据类型转换，布尔值转化为float32，true = 1， false = 0
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    tf.global_variables_initializer().run()

    validate_feed = {x: mnist.validation.images, y_: mnist.validation.labels}
    test_feed = {x: mnist.test.images, y_: mnist.test.labels}

    for i in range(30000):
        if i % 1000 == 0:
            validate_accuracy = sess.run(accuracy, feed_dict=validate_feed)
            print('After %d training steps %g%%' % (i, validate_accuracy*100))
        xs, ys = mnist.train.next_batch(100)
        sess.run(train_op, feed_dict={x: xs, y_: ys})

    test_accuracy = sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})
    print('accuracy:', test_accuracy*100)

"""
两层MLP，
"""


from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

mnist = input_data.read_data_sets('../MNIST_data', one_hot=True)
batch_size = 100
learning_rate = 0.8
learning_rate_decay = 0.99
max_steps = 30000
training_step = tf.Variable(0, trainable=False)


def hidden_layer(input_tensor, w1, b1, w2, b2, layer_name):
    layer1 = tf.nn.relu(tf.matmul(input_tensor, w1) + b1)
    return tf.matmul(layer1, w2) + b2


x = tf.placeholder(tf.float32, [None, 784], name="x-input")
y_ = tf.placeholder(tf.float32, [None, 10], name="y-label")

w1 = tf.Variable(tf.truncated_normal([784, 500], stddev=0.1))
b1 = tf.Variable(tf.constant(0.1, shape=[500]))
w2 = tf.Variable(tf.truncated_normal([500, 10], stddev=0.1))
b2 = tf.Variable(tf.constant(0.1, shape=[10]))

y = hidden_layer(x, w1, b1, w2, b2, "y-output")
# 初始化一个滑动平均类，为了模型在训练前期可以更新更快
average_class = tf.train.ExponentialMovingAverage(0.99, training_step)
# 定义一个更新变量滑动平均值的操作，需要向滑动平均类的apply提供一个参数列表（被优化的参数）
average_op = average_class.apply(tf.trainable_variables())
# 得到优化后的y值
average_y = hidden_layer(x, average_class.average(w1), average_class.average(b1), average_class.average(w2),
                         average_class.average(b2), "average-y")

# 计算交叉熵损失
cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.argmax(y_, 1))
# 引入l2正则化
regularizer = tf.contrib.layers.l2_regularizer(0.001)
regularization = regularizer(w1) + regularizer(w2)
loss = tf.reduce_mean(cross_entropy) + regularization
# 用指数衰减法设置学习率
learning_rate = tf.train.exponential_decay(learning_rate, training_step, mnist.train.num_examples/batch_size, learning_rate_decay)
train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step=training_step)
# 更新每一个参数的滑动平均值
with tf.control_dependencies([train_step, average_op]):
    train_op = tf.no_op(name='train')
# argmax(y,1):在x的第一个维度选择最大值，返回最大值的坐标索引
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


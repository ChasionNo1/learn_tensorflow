"""
LeNet-5网络：

"""
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data


mnist = input_data.read_data_sets("./MNIST_data", one_hot=True)


batch_size = 128
dropout = 0.5
learning_rate = 1e-3
l2_lambda = 1e-5


x = tf.placeholder(tf.float32, [None, 28*28])
y_ = tf.placeholder(tf.float32, [None, 10])
keep_prob = tf.placeholder(tf.float32)


def conv2d(inp, w, b, strides=1):
    kernel = tf.Variable(tf.random_normal(shape=w))
    biases = tf.Variable(tf.random_normal(shape=b))
    out = tf.nn.conv2d(inp, kernel, strides=[1, strides, strides, 1], padding='VALID')
    out = tf.nn.bias_add(out, biases)
    return tf.maximum(0.1*out, out)


def conv_layer(inp, out_map, kernel_size, strides, padding):
    '''
    conv = tf.layers.conv2d(image, 24, 5, 2, 'same')
    :return: feature map
    '''
    conv_out = tf.layers.conv2d(inp, out_map, kernel_size, strides, padding, use_bias=True)
    return tf.maximum(0.1*conv_out, conv_out)


def max_pooling(inp, ksize, strides):
    # max_pool = tf.nn.max_pool(conv1, ksize=[1, 2, 2, 1], strides=[1, 1, 1, 1], name='max-pool', padding='SAME')
    return tf.nn.max_pool(inp, ksize, strides, padding='VALID')


def fc(inp, num_out, name):
    # 得到输入数据的维数
    # 池化层的输出结果是什么样的？
    # 3*3*64 特征图的大小和个数

    dim = inp.get_shape()[1].value
    # print(dim, num_out) 120 84
    w = tf.Variable(tf.random_normal(shape=[dim, num_out]))
    b = tf.Variable(tf.random_normal(shape=[num_out]))
    fc_out = tf.add(tf.matmul(inp, w), b)
    return tf.maximum(0.1*fc_out, fc_out)


def lenet_5(inp, prob):
    # print(inp.shape)
    x = tf.reshape(inp, [-1, 28, 28, 1])
    # print(x.shape)
    x = tf.pad(x, [[0, 0], [2, 2], [2, 2], [0, 0]])
    # conv1 = conv_layer(x, 6, 5, 1, 'valid')
    conv1 = conv2d(x, [5, 5, 1, 6], [6])
    pool2 = max_pooling(conv1, [1, 2, 2, 1], [1, 2, 2, 1])
    # conv3 = conv_layer(pool2, 16, 5, 1, 'valid')
    conv3 = conv2d(pool2, [5, 5, 6, 16], [16])
    pool4 = max_pooling(conv3, [1, 2, 2, 1], [1, 2, 2, 1])
    # conv5 = conv_layer(pool4, 120, 5, 1, 'valid')
    conv5 = conv2d(pool4, [5, 5, 16, 120], [120])
    conv6 = tf.contrib.layers.flatten(conv5)
    fc6 = fc(conv6, 84, 'fc6')
    fc7 = fc(fc6, 10, 'fc7')
    fc8 = tf.nn.dropout(fc7, dropout)
    return fc8


logits = lenet_5(x, keep_prob)
# prediction = tf.nn.softmax(logits)
loss_op = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logits, labels=y_))
l2_loss = tf.contrib.layers.apply_regularization(regularizer=tf.contrib.layers.l2_regularizer(l2_lambda), weights_list=tf.trainable_variables())
final_loss = loss_op + l2_loss
train_op = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(final_loss)

correct_pred = tf.equal(tf.argmax(logits, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

with tf.Session() as sess:
    tf.global_variables_initializer().run()
    X_test = mnist.test.images[:10000]
    Y_test = mnist.test.labels[:10000]
    for i in range(1, 30001):
        batch_x, batch_y = mnist.train.next_batch(batch_size)
        sess.run(train_op, feed_dict={x: batch_x, y_: batch_y, keep_prob: dropout})
        if i % 10 == 0:
            loss, acc = sess.run([loss_op, accuracy], feed_dict={x: batch_x, y_: batch_y, keep_prob: 1.0})
            print('step:' + str(i) + ',minibatch_loss:{:.4f}'.format(loss) + ',accuracy:{:.4f}'.format(acc))

        if i % 500 == 0 and i > 10000:
            print("Test Step "+str(i)+": Accuracy:",  \
            sess.run(accuracy, feed_dict={x: X_test, y_: Y_test, keep_prob: 1.0}))








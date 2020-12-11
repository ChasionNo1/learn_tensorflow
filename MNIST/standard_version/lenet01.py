import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("./MNIST_data", one_hot=True)

batch_size = 128
learning_rate = 1e-3
display_step = 100
test_step = 500
num_steps = 30000
dropout = 0.5
l2_lambda = 1e-5

X = tf.placeholder(tf.float32, [None, 28*28])
Y = tf.placeholder(tf.float32, [None, 10])
keep_prob = tf.placeholder(tf.float32)


def conv2d(x, W, b, strides=1):
    filter_weights = tf.Variable(tf.random_normal(shape=W))
    conv_bias = tf.Variable(tf.random_normal(shape=b))
    x = tf.nn.conv2d(x, filter_weights, strides=[1, strides, strides, 1], padding='VALID')
    x = tf.nn.bias_add(x, conv_bias)
    return tf.maximum(0.1*x, x)


def maxpool2d(x, k=2):
    return tf.nn.max_pool(x, ksize=[1, k, k, 1], strides=[1, k, k, 1], padding='VALID')


def fc(x, W, b):
    fc_filter = tf.Variable(tf.random_normal(shape=W))
    fc_bias = tf.Variable(tf.random_normal(shape=b))
    x = tf.add(tf.matmul(x, fc_filter), fc_bias)
    return tf.maximum(0.1*x, x)


def lenet(X, dropout):
    x = tf.reshape(X, [-1, 28, 28, 1])
    # print(x.shape)
    x = tf.pad(x, [[0, 0], [2, 2], [2, 2], [0, 0]])
    # conv1 = conv_layer(x, 6, 5, 1, 'valid')
    conv1 = conv2d(x, [5, 5, 1, 6], [6])
    pool2 = maxpool2d(conv1)
    # conv3 = conv_layer(pool2, 16, 5, 1, 'valid')
    conv3 = conv2d(pool2, [5, 5, 6, 16], [16])
    pool4 = maxpool2d(conv3)
    # conv5 = conv_layer(pool4, 120, 5, 1, 'valid')
    conv5 = conv2d(pool4, [5, 5, 16, 120], [120])
    conv6 = tf.contrib.layers.flatten(conv5)
    fc6 = fc(conv6, [120, 84], [84])
    fc7 = fc(fc6, [84, 10], [10])
    fc8 = tf.nn.dropout(fc7, dropout)
    return fc8

# weights = {
#     'conv1' : tf.Variable(tf.random_normal([5, 5, 1, 6])),
#     'conv3' : tf.Variable(tf.random_normal([5, 5, 6, 16])),
#     'conv5' : tf.Variable(tf.random_normal([5, 5, 16, 120])),
#     'fc6' : tf.Variable(tf.random_normal([120, 84])),
#     'fc7' : tf.Variable(tf.random_normal([84, 10]))
# }
# biases = {
#     'conv1' : tf.Variable(tf.random_normal([6])),
#     'conv3' : tf.Variable(tf.random_normal([16])),
#     'conv5' : tf.Variable(tf.random_normal([120])),
#     'fc6' : tf.Variable(tf.random_normal([84])),
#     'fc7' : tf.Variable(tf.random_normal([10]))
# }


logits = lenet(X, keep_prob)
prediction = tf.nn.softmax(logits)

loss_op = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
    logits=logits, labels=Y))
l2_loss = tf.contrib.layers.apply_regularization(regularizer=tf.contrib.layers.l2_regularizer(l2_lambda), weights_list=tf.trainable_variables())
final_loss = loss_op + l2_loss
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)
train_op = optimizer.minimize(final_loss)

correct_pred = tf.equal(tf.argmax(prediction, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
init = tf.global_variables_initializer()

saver = tf.train.Saver(max_to_keep=1)
if __name__ == '__main__':
    with tf.Session() as sess:
        sess.run(init)
        X_test = mnist.test.images[:10000]
        Y_test = mnist.test.labels[:10000]
        for step in range(1, num_steps + 1):
            batch_x, batch_y = mnist.train.next_batch(batch_size)
            sess.run(train_op, feed_dict={X: batch_x, Y: batch_y, keep_prob: dropout})
            if step % display_step == 0 or step == 1:
                pre, loss, acc = sess.run([prediction, loss_op, accuracy], feed_dict={X: batch_x, Y: batch_y, keep_prob: 1.0})
                print("Step " + str(step) + \
                      ", Minibatch Loss= " + "{:.4f}".format(loss) + \
                      ", Training Accuracy= " + "{:.3f}".format(acc))

            if step % test_step == 0 and step > 10000:
                accu = sess.run(accuracy, feed_dict={X: X_test, Y: Y_test, keep_prob: 1.0})
                print("Test Step " + str(step) + ": Accuracy:" + "{:.3f}".format(accu))
        saver.save(sess, './weights/mnist_model.ckpt')

        print("Optimization Finished!")


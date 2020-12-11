import tensorflow as tf
import numpy as np
import cv2
import lenet01
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('../MNIST_data', one_hot=True)


'''
预测思路：
加载模型，然后输入一个图片，得到预测结果 
'''


def prediction():
    tf.reset_default_graph()
    x = tf.placeholder(tf.float32, shape=[None, 28*28])
    y_ = tf.placeholder(tf.float32, shape=[None, 10])
    inp = tf.reshape(x, shape=[-1, 28, 28, 1])
    y = lenet01.lenet(inp, 1.0)
    y_softmax = tf.nn.softmax(y)
    correct_pred = tf.equal(tf.argmax(y_softmax, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

    saver = tf.train.Saver()

    with tf.Session() as sess:
        saver.restore(sess, './weights/mnist_model.ckpt')
        X_test = mnist.test.images[0:20]
        Y_labels = mnist.test.labels[0:20]

        # 可以加一个读1.png的结果
        image = cv2.imread('./1.png')
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image, (28, 28))
        array = np.array(image)
        re = array.reshape([1, 28*28])
        result2 = sess.run(y_softmax, feed_dict={x: re})
        print(sess.run(tf.argmax(result2, axis=1)) + 1)
        result = sess.run(y_softmax, feed_dict={x: X_test})
        print(sess.run(tf.argmax(Y_labels, axis=1)) + 1)
        print(sess.run(tf.argmax(result, axis=1)) + 1)

        # for i in result:
        #     print('预测值：', i)
        # print(result)
        # acc = sess.run(accuracy, feed_dict={x: X_test, y_: Y_labels})
        # print('{:.3f}'.format(acc*100))


prediction()

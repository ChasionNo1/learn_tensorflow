"""
常用激活函数： relu, Prelu,sigmoid, tanh
"""
import tensorflow as tf


def simgoid(x):
    return 1/(1+tf.exp(-x))


def tanh(x):
    return (tf.exp(x)-tf.exp(-x))/(tf.exp(x)+tf.exp(-x))


data = None
tf.nn.relu(data)
tf.nn.tanh(data)
tf.nn.sigmoid(data)




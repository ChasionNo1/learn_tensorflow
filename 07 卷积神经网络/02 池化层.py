"""
池化层
"""
import tensorflow as tf


def max_pooling(inp, k_h, k_w, s_h, s_w, name, padding='SAME'):
    return tf.nn.max_pool(inp,
                          ksize=[1, k_h, k_w, 1],
                          strides=[1, s_h, s_w, 1],
                          name=name,
                          padding=padding
                          )


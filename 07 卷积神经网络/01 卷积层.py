import tensorflow as tf
import cv2
'''
tf.layers.conv2d(inputs, filters, kernel_size,
    strides=(1, 1),
    padding='valid',
    data_format='channels_last',
    dilation_rate=(1, 1),
    activation=None,
    use_bias=True,
    kernel_initializer=None,
    bias_initializer=None,
    kernel_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    bias_constraint=None,
    trainable=True,
    name=None,
    reuse=None)

（1） input：指需要做卷积的输入图像，要求是一个Tensor，具有[batch,in_height,in_width,in_channels]这样的图像，具体含义是“训练时一个batch的图片数量，图片的高度，图片的宽度，图像通道数”，注意：这是一个四维的Tensor，要求类型为float32和float64之一
（2） filters： 整数,输出空间的维数(即卷积中的滤波器数).
（3） kernel_size:滤波器的大小，如果是一个整数，则宽高相等。
（4）strides：一个整数，或者包含了两个整数的元组/队列，表示卷积的纵向和横向的步长。如果是一个整数，则横纵步长相等。另外， strides 不等于1 和 dilation_rate 不等于1 这两种情况不能同时存在。
（5）padding：定义元素边框与元素内容之间的空间，“valid” 或者 “same”（不区分大小写）。“valid” 表示边缘不填充，"same"表示填充到过滤器可以达到图像边缘，注：在same情况下，只有在步长为1时生成的feature map才会和输入值相等。



tf.nn.conv2d(input, filter, strides, padding, use_cudnn_on_gpu=None, name=None)
第一个参数input：指需要做卷积的输入图像，它要求是一个Tensor，具有[batch, in_height, in_width, in_channels]这样的shape，
具体含义是[训练时一个batch的图片数量, 图片高度, 图片宽度, 图像通道数]，注意这是一个4维的Tensor，要求类型为float32和float64其中之一

第二个参数filter：相当于CNN中的卷积核，它要求是一个Tensor，具有[filter_height, filter_width, in_channels, out_channels]这样的shape，
具体含义是[卷积核的高度，卷积核的宽度，图像通道数，卷积核个数]，要求类型与参数input相同，有一个地方需要注意，第三维in_channels，就是参数input的第四维

第三个参数strides：卷积时在图像每一维的步长，这是一个一维的向量，长度4
第四个参数padding：string类型的量，只能是"SAME","VALID"其中之一，这个值决定了不同的卷积方式（后面会介绍）
第五个参数：use_cudnn_on_gpu:bool类型，是否使用cudnn加速，默认为true
结果返回一个Tensor，这个输出，就是我们常说的feature map

说明：input和filter都是tensor，需要初始化
'''

'''
函数的一些说明，input必须是4维的[batch_size, height, weight, channels]
输入数据类型为tf.float32
卷积核大小和填充方式的关系，以及步长的关系

'''
image = cv2.imread('./test01.jpg')
# (300, 533, 3)
# print(image.shape)
# cv2.imshow('iamge', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# iamge = tf.reshape(image, shape=[1, 300, 533, 3])
image = tf.expand_dims(image, axis=0)
image = tf.cast(image, tf.float32)
conv = tf.layers.conv2d(image, 24, 5, 2, 'same')
# (1, 300, 533, 24)
# print('conv_shape:', conv.get_shape())
# input, filter, strides, padding, use_cudnn_on_gpu=None, name=None
# filter_height, filter_width, in_channels, out_channels
# (1, 300, 533, 3)
kernel = tf.Variable(tf.random_normal([5, 5, 3, 24]))
conv1 = tf.nn.conv2d(image, kernel, [1, 2, 2, 1], padding='SAME', name='conv-2')
# inp,
# ksize=[1, k_h, k_w, 1],
# strides=[1, s_h, s_w, 1],
# name=name,
# padding=padding
max_pool = tf.nn.max_pool(conv1, ksize=[1, 2, 2, 1], strides=[1, 1, 1, 1], name='max-pool', padding='SAME')
# max-pool_shape: (1, 150, 267, 24)
# print('max-pool_shape:', max_pool.get_shape())
# (1, 150, 267, 24)
# print('conv1_shape:', conv1.shape)

# 全连接层的实现
reshape = tf.reshape(max_pool, [1, -1])
dim = reshape.get_shape()[1].value
# print(dim)
w = tf.Variable(tf.random_normal(shape=[dim, 20], stddev=0.1))
b = tf.Variable(tf.constant(0.1, shape=[20]))
fc = tf.nn.relu(tf.matmul(reshape, w) + b)

# softmax，交叉熵损失函数

with tf.Session() as sess:
    tf.global_variables_initializer().run()
    print(sess.run(conv1))
    print(sess.run(conv))
    print(sess.run(max_pool))
    print(sess.run(fc))


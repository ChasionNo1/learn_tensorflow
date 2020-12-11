"""
文件说明

get_variable()函数：创建变量，或者通过获取已经创建的变量来创建变量
get_variable(name,shape,dtype,initializer,regularizer,trainable,collections,caching_device,partitioner,validate_shape,custom_getter)

"""
import tensorflow as tf


a = tf.compat.v1.Variable(tf.compat.v1.constant(1.0, shape=1, name="a"))
b = tf.compat.v1.get_variable("b", shape=1, initializer=tf.compat.v1.constant_initializer(1.0))

'''初始化变量函数'''
# 将变量初始化为给定的常量
tf.compat.v1.constant_initializer()
# 将变量初始化为满足正太分布的随机数值
tf.compat.v1.random_normal_initializer()
# 将变量初始化为满足正太分布的随机数值，但如果随机出来的值偏离平均值超过两个标准差，就重随
tf.compat.v1.truncated_normal_initializer()
# 平均分布的随机数值
tf.compat.v1.random_uniform_initializer()
# 平均分布但不影响输出数量级的随机数值
tf.compat.v1.uniform_unit_scaling_initializer()
# 初始化全为1
tf.compat.v1.zeros_initializer()
# 初始化全为0
tf.compat.v1.ones_initializer()

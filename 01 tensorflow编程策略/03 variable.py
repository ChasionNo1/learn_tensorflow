"""
文件说明

创建变量，保存网络中的参数

"""
import tensorflow as tf

# 声明变量时需要设置初始值，可以设置成随机数
# random_normal:大小为3*4，元素均值为0，标准差为1的随机数矩阵
weights = tf.compat.v1.Variable(tf.compat.v1.random_normal([3, 4], stddev=1))
# 正太分布
# tf.compat.v1.random_normal(shape,mean,stddev,dtype,seed,name) 形状、平均值、标准差、数值类型、随机种子、名称

# 正太分布，如果随机出来的值偏离平均值超过两个标准差，那么这个数将会被重新随机，参数和random_normal一样
tf.compat.v1.truncated_normal()

# 平均分布,  shape,minval,maxval,stddev,dtype,seed,name  最小值和最大值
tf.compat.v1.random_uniform()

# Gamma分布, shape,alpha,beta,stddev,dtype,seed,name  形状参数alpha，尺度参数beta
tf.compat.v1.random_gamma()


'''常数生成函数'''
# 产生全是0的数组，shape，dtype，name
tf.compat.v1.zeros()
# 产生全是1的数组，shape，dtype，name
tf.compat.v1.ones()
# 产生一个值为给定数字的数组,dims,value,name:维度、数值、名称
tf.compat.v1.fill()
# 产生一个给定值的常量,value,dtype,shape,name,verity_shape
tf.compat.v1.constant()
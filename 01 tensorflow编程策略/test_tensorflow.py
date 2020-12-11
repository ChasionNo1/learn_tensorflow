"""
文件说明:测试tensorflow安装，版本为1.14

"""
import tensorflow as tf

# 定义两个张量
a = tf.constant([1.0, 2.0], name='a')
b = tf.constant([3.0, 4.0], name='b')
# 求和
result = a + b
# 开启会话
sess = tf.compat.v1.Session()
# 运行
print(sess.run(result))  # [4. 6.]

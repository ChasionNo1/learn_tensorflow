"""
文件说明

"""
import tensorflow as tf

# # 在名为one的变量空间内创建一个名字为a的变量
# with tf.compat.v1.variable_scope("one"):
#     a = tf.compat.v1.get_variable("a", shape=1, initializer=tf.compat.v1.constant_initializer(1.0))


'''
在相同的变量空间内使用get_variable()创建name属性相同的两个变量会报错，
variable_scope的参数reuse默认值为false，当为true的时候，这个上下文管理器内所以get_variable()函数都会直接
获取name相同的已经创建的变量，如果没有就报错
false是，创建新的变量，如果存在就报错
'''

'''变量空间的嵌套'''
a = tf.compat.v1.get_variable("a", shape=1, initializer=tf.compat.v1.constant_initializer(1.0))
# a:0  a是变量名，0是生成这个变量运算的第一个结果
print(a.name)

with tf.compat.v1.variable_scope("one"):
    a2 = tf.compat.v1.get_variable("a", shape=1, initializer=tf.compat.v1.constant_initializer(1.0))
    # one/a:0
    print(a2.name)
    # get_variable_scope可以获取当前的变量空间
    print(tf.compat.v1.get_variable_scope().reuse)

with tf.compat.v1.variable_scope("one"):
    with tf.compat.v1.variable_scope("two"):
        a4 = tf.compat.v1.get_variable("a", shape=1, initializer=tf.compat.v1.constant_initializer(1.0))
        # one/two/a:0
        print(a4.name)
        # 在一个嵌套的变量空间中如果不指定reuse参数，那么会默认和外面最近的一层保持一致
        print(tf.compat.v1.get_variable_scope().reuse)
    b = tf.compat.v1.get_variable("b", 1)
    # one/b:0
    print(b.name)
with tf.compat.v1.variable_scope("", reuse=True):
    a5 = tf.compat.v1.get_variable("one/two/a", 1)
    # True
    print(a5 == a4)


'''
name_scope内部使用get_variable()，生成的变量名不会被添加变量空间的前缀，而Variable()会添加
variable_scope，两个函数都会添加前缀
name_scope没有reuse参数
name_scope用于可视化计算图
'''


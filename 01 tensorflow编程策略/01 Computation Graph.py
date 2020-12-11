"""
文件说明
tensorflow计算过程可以表示为一个计算图（有向图），类似于流程图，可以直观看出数据的计算流程
每一个运算操作可以视为一个节点，每一个节点可以有任意输入输出
张量（tensor）就是在边中流动（flow）的数据，可以理解为数组，
计算图---tensorflow的计算模型

创建会话的两种方式：
sess = tf.compat.v1.Session
sess.run()
sess.close()

with/as环境上下文管理器

直接构建默认会话：tf.InteractiveSession()

eval和run的使用：用于运行会话（计算张量的值）
sess.run(result)
result.eval()
如果sess不是默认的会话，那么在执行的时候需要指明会话
result.eval(session=sess)
区别：
t.eval() 等价于 tf.get_default_session().run(t)
run()函数可以传入多个需要计算的张量，eval只能计算一个张量就调用一次eval函数

Session的参数配置：
config参数：配置会话的并行线程数、GPU分配策略、运算超时时间
ConfigProto()函数配置Session：
config = tf.ConfigSession(log_device_placement=True, allow_soft_lacement=True)
log_device_placement:日志中将会记录运行每个节点所用的计算设备，然后打印出来
allow_soft_lacement：当运行无法在GPU上执行的时候转移到CPU上执行
sess = tf.Session(config = config)

placeholder机制：


"""
import tensorflow as tf
# 使用graph创建一个计算图
g1 = tf.Graph()
# 设置为默认计算图
with g1.as_default():
    # 创建变量设置初始值
    a = tf.compat.v1.get_variable("a", [2], initializer=tf.ones_initializer())
    b = tf.compat.v1.get_variable("b", [2], initializer=tf.zeros_initializer())
# 开启会话，初始化计算图中的所有变量
with tf.compat.v1.Session(graph=g1) as sess:
    tf.compat.v1.global_variables_initializer().run()
    # 控制变量空间
    with tf.compat.v1.variable_scope("", reuse=True):
        print(sess.run(tf.compat.v1.get_variable("a")))  # [1. 1.]
        print(sess.run(tf.compat.v1.get_variable("b")))  # [0. 0.]

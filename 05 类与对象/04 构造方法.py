"""
文件说明

"""


class InConstructor:
    def __init__(self):
        # 在构造方法中定义一个foo变量
        foo = 0
        # 使用self代表该构造方法正在初始化的对象
        # 下面的代码将会把该构造方法正在初始化的对象的foo实例变量设为6
        self.foo = 6


# 所有使用InConstructor创建的对象的foo实例变量都被设为6
print(InConstructor().foo)



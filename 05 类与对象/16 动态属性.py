"""
文件说明

"""


class Cat:
    def __init__(self, name):
        self.name = name


def walk_func(self):
    print('%s慢慢地走过一片草地' % self.name)


d1 = Cat('a')
d2 = Cat('b')
# 为cat动态添加walk方法，该方法的第一个参数会自动绑定
# 为类动态添加方法时不需要使用MethodType进行包装
Cat.walk = walk_func
d1.walk()
d2.walk()

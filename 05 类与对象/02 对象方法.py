"""
文件说明

"""
from types import MethodType


class Person:
    # 定义类变量
    hair = 'black'

    def __init__(self, name='ccc', age=3):
        # 为Person对象添加两个实例变量
        self.name = name
        self.age = age


def info(self):
    print('---info函数-----', self)


p = Person()
# 使用info对p的foo方法赋值（动态增加方法）
p.foo = info
# python不会自动将调用者绑定到第一个参数，需要手动添加
p.foo(p)

# 使用lambda表达式为p对象的bar方法赋值
p.bar = lambda self: print('---bar方法---', self)
p.bar(p)

# 借助types模块下的MethodType进行包装，自动绑定
p.intro = MethodType(info, p)

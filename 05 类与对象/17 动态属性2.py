"""
文件说明

"""
from types import MethodType


class Dog:
    __slots__ = ('walk', 'age', 'name')

    def __init__(self, name):
        self.name = name

    def test(self):
        print('test方法')


d = Dog('as')
d.walk = MethodType(lambda self: print('%s 正在慢慢走' % self.name), d)
d.age = 5
d.walk()

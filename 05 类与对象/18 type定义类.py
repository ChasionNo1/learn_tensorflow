"""
文件说明

"""


def fn(self):
    print('fn函数')


# 使用type定义Dog类
Dog = type('Dog', (object,), dict(walk = fn, age = 6))
d = Dog()
print(type(d))
print(type(Dog))
d.walk()
print(Dog.age)
'''
<class '__main__.Dog'>
<class 'type'>
fn函数
6
'''


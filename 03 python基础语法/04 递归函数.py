"""
文件说明

"""
import sys
sys.setrecursionlimit(50000)


def get_fn(n):
    if n > 1:
        return n*get_fn(n-1)
    else:
        return 1


print(get_fn(10))


def get_sum(a, b):
    return a+b


get_sum(1, 2)


def say(name='123', message='122'):
    print(name, ',你好')
    print('message:', message)


say()
say('768')
say(message='nice')
'''
123 ,你好
message: 122
768 ,你好
message: 122
123 ,你好
message: nice
'''


def show(*name):
    for i in name:
        print(i)


show(1, 24, 2, 'sio')

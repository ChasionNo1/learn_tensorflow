"""
文件说明

"""


def foo(fn):
    def bar(*args):
        print('----1-----', args)
        n = args[0]
        print('-------2---------', n*(n-1))
        # 查看传给foo函数的fn函数
        print(fn.__name__)
        fn(n*(n-1))
        print('*'*15)
        return fn(n*(n-1))
    return bar

@foo
def my_test(a):
    print('---my_test----', a)


print(my_test)
my_test(10)
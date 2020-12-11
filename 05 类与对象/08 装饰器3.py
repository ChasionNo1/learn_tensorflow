"""
文件说明
在被修饰函数之前、之后抛出异常后增加某种处理逻辑的方式，就是面向切面编程
通过函数装饰器为函数添加权限检查的功能

"""


def auth(fn):
    def auth_fn(*args):
        # 用一条语句模拟执行权限检查
        print('----权限检查------')
        # 回调被修饰的目标函数
        fn(*args)
    return auth_fn


@auth
def test(a, b):
    print('执行test函数，参数a: %s, 参数b: %s' % (a,b))


# 调用test函数，其实就是调用修饰后返回的auth_fn函数
test(20, 15)


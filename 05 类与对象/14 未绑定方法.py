"""
文件说明

"""


class BaseClass:
    def foo(self):
        print('父类中定义的foo方法')


class SubClass(BaseClass):
    def foo(self):
        print('子类重写父类中的foo方法')

    def bar(self):
        print('bar方法')
        # 直接执行foo方法，将会调用子类重写的foo方法
        self.foo()
        # 使用类名调用实例方法（未绑定方法）调用父类的foo方法
        BaseClass.foo(self)


sc = SubClass()
sc.bar()

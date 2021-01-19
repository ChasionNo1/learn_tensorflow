"""
文件说明
前后均带有双下划线__的命名
一般用于特殊方法的命名，用来实现对象的一些行为或者功能，比如__new__()方法用来创建实例，__init__()方法用来初始化对象，

仅开头带双下划线__的命名
用于对象的数据封装，以此命名的属性或者方法为类的私有属性或者私有方法。

以单下划线_开头的命名
一般用于模块中的"私有"定义的命名。在类中也可以用单下划线开头来命名属性或者方法，这只是表示类的定义者希望这些属性或者方法是"私有的"，但实际上并不会起任何作用。
"""


class User:
    def __hide(self):
        print('隐藏的hide方法')

    def getname(self):
        return self.__name

    def setname(self, name):
        if len(name) < 3 or len(name) > 8:
            raise ValueError('用户名长度必须在3-8之间')
        self.__name = name

    name = property(getname, setname)

    def setage(self, age):
        if age < 18 or age > 70:
            raise ValueError('用户年龄必须在18-70之间')
        self.__age = age

    def getage(self):
        return self.__age

    age = property(getage, setage)


u = User()
u.name = 'allg'
# u._User__hide()

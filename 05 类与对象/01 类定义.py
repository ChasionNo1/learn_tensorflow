"""
文件说明

Python 类名必须是由一个或多个有意义的单词连缀而成的，每个单词首字母大写，其他字母全部小写，单词与单词之间不要使用任何分隔符
在类体中最主要的两个成员就是类变量和方法 如果不为类定义任何类变量和方法,那么这个类就相当于一个空类,
如果空类不需要其他可执行语句,则可使用 pass语句作为占位符
类中各成员之间的定义顺序没有任何影向，各成员之间可以相互调用
Python 类所包含的最重要的两个成员就是变量和方法,其中类变 属于类本身,用于定义该 类本身所包含的状态数据：
而实例变 则属于该类的对象,用于定义对象所包含的状态数据：方法 则用于定义该类的对象的行为或功能实现
"""


class Person:
    # 定义类变量
    hair = 'black'

    def __init__(self, name='ccc', age=3):
        # 为Person对象添加两个实例变量
        self.name = name
        self.age = age

    def say(self, content):
        print(content)


p = Person()
print(p.name, p.age)
p.say('safdsg')
p.name = 'a'
print(p.name)
# 为p增加一个skills实例变量
p.skills = ['1']
print(p.skills)
# 删除p对象的name实例变量
del p.name

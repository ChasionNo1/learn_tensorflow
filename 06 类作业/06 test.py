"""
文件说明

"""


class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def talk(self):
        print('我是%s ，我的价格是%s' % (self.name, self.price))


d = Car('badou', 12333)
d.talk()


class Vehicle:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print('我是：%s' % self.name)

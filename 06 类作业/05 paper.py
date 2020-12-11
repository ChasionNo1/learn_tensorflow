"""
文件说明

"""


class Vehicle:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print('我是：%s' % self.name)


class Car(Vehicle):
    def __init__(self, name, price):
        super().__init__(name)
        self.price = price

    def talk(self):
        print('我是：%s, 我的价格是：%s' % (self.name, self.price))


car = Car('宝马', 12333)
car.talk()




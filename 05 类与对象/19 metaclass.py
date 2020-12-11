"""
文件说明

"""


class ItemMetaClass(type):
    # cls代表被动态修改的类，name代表被动态修改的类名，bases代表被动态修改的类的所以父类
    # attr代表被动态修改的类的所有属性、方法组成的字典
    # metaclass类的new方法的作用是：当程序使用class定义新类时，如果指定了metaclass，
    # 那么metaclass的new方法就会被执行
    def __new__(cls, name, baeses, attrs):
        attrs['cal_price'] = lambda self: self.price * self.discount
        return type.__new__(cls, name, baeses, attrs)


class Book(metaclass=ItemMetaClass):
    __slots__ = ('name', 'price', '_discount')

    def __int__(self, name, price):
        self.name = name
        self.price = price

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        self._discount = discount


class CellPhone(metaclass=ItemMetaClass):
    __slots__ = ('price', '_discount')

    def __init__(self, price):
        self.price = price

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        self._discount = discount


b = Book()
b.name = 'python手册'
b.price = 89
b.discount = 0.76
print(b.cal_price())
cp = CellPhone(2399)
cp.discount = 0.95
print(cp.cal_price())




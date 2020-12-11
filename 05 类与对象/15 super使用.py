"""
文件说明

"""


class Employee:
    def __init__(self, salary):
        self.salary = salary

    def work(self):
        print('普通员工正在写代码，工资是：', self.salary)


class Customer:
    def __init__(self, favorite, address):
        self.favorite = favorite
        self.address = address

    def info(self):
        print('顾客的喜好是：%s，地址是：%s' % (self.favorite, self.address))


class Manager(Employee, Customer):
    # 重写父类的构造方法
    def __init__(self, salary, favorite, address):
        print('----manager的构造方法')
        super().__init__(salary)
        # super(Manager, self).__init__(salary) 和上一行代码效果相同
        # 因为super会优先继承第一个父类，所以这里的super是Employee的，而第二个父类的init需要通过使用未绑定方法来重写
        Customer.__init__(self, favorite, address)
        # super().__init__(favorite, address) 错误：__init__() takes 2 positional arguments but 3 were given
        # super(Customer, self).__init__(favorite, address)  object.__init__() takes exactly one argument (the instance to initialize)


m = Manager(25000, 'it', 'guangzhou')
m.work()
m.info()

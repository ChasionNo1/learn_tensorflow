"""
文件说明

"""


class Bird:
    def fly(self):
        print('我在天空里自由自在的飞翔')


class Ostrich(Bird):
    def fly(self):
        print('我只能在地上跑')


ostrich = Ostrich()
ostrich.fly()

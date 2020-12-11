"""
文件说明

"""


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


d = Dog('旺财', 18)
print(d.name)
print(d.age)
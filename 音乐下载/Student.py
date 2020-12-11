"""
文件说明

1．编写一个学生类，提供name、age、gender、phone、address、email等属性，为学生类提供
  带所有成员变量的构造器，为学生类提供方法，用于描绘吃、喝、玩、睡等行为。
"""


class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @property
    def detail_info(self):
        return self._phone,

    @detail_info.setter
    def detail_info(self, phone):
        self._phone = phone

    def eat(self):
        print('%s在吃饭' % self.name)

    def drink(self):
        print('%s在喝可乐' % self.name)



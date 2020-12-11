"""
文件说明

"""


class Rectangle:
    # 定义构造方法
    def __init__(self,width,height):
        self.width = width
        self.height = height
    # 定义setsize函数

    def setsize(self, size):
        self.width,self.height = size

    # 定义getsize函数
    def getsize(self):
        return self.width, self.height

    # 定义delsize函数
    def delsize(self):
        self.width, self.height = 0, 0

    # 使用property定义属性
    size = property(getsize, setsize, delsize, doc='用于描述矩形大小的属性')


print(Rectangle.size.__doc__)
# 通过help函数查看Rectangle.size的说明文档
help(Rectangle.size)
rect = Rectangle(3, 4)
print(rect.size)
rect.size = 9, 7
print(rect.width)
print(rect.height)
del rect.size
print(rect.width)
print(rect.height)

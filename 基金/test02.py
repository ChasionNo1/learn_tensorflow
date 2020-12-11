"""
文件说明

"""
from decimal import Decimal


a = Decimal('-0.32')
b = Decimal('1.32')
# ValueError: invalid literal for int() with base 10: '-0.32'
# 需要进行判断，负号就是减法运算，starwith()
print(a+b)

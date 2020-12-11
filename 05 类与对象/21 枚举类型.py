"""
文件说明

"""
from enum import Enum
import enum


class Color(Enum):
    # 成员值可以为任意类型: int, str 等等。
    # 如果具体的值不重要，你可以使用 auto 实例，将为你选择适当的值。
    # 但如果你混用 auto 与其他值则需要小心谨慎。
    # 不允许有同名的枚举成员
    RED = 1
    GREEN = 2


# 遍历所有的成员
for name, member in Color.__members__.items():
    print(member, '-->', name, '---->', member.value)


# 通过使用Enum列举多个枚举值来创建枚举四季类
Season = enum.Enum('Season', ('S', 'A', 'B', 'F'))
print(Season.S)
print(Season.S.name)
print(Season.S.value)



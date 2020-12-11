"""
文件说明
定义一个 isleap(year) 函数,该函数可判断 year 是否为闰年.若是闰年,则返回 True；否则返回 False
闰年的定义：
公历年份是4的倍数的，且不是100的倍数，为普通闰年。
公历年份是整百数的，必须是400的倍数才是世纪闰年
"""


def isleap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


print(isleap(2000))

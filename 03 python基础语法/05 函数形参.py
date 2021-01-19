"""
文件说明

"""


def deal_map(data,fn):
    result = []
    for e in data:
        result.append(fn(e))
    return result


def square(n):
    return n*n


def cube(n):
    return n*n*n


def factorial(n):
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result


data = [3, 3, 9, 5]
print(deal_map(data, square))
print(deal_map(data, cube))

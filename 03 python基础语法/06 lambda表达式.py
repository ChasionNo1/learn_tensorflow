"""
文件说明

"""


def get_math_func(type):
    result = 1
    if type == 'cube':
        return lambda n: n*n*n
    else:
        return lambda n: n*n


math_func = get_math_func('cube')
print(math_func(4))

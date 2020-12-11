"""
文件说明

"""


def get_result(a, b):
    return a+b, a-b


sum_result, sub_result = get_result(12, 4)
# 16 8
print(sum_result, sub_result)
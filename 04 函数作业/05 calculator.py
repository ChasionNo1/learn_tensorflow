"""
文件说明

"""
import random


def math_func(select_type, n):
    if select_type == 'cubic':
        return sum([i*i*i for i in range(1, n+1)])
    if select_type == 'factorial':
        result = 1
        for i in range(1, n+1):
            result = result * i
        return result
    if select_type == 'get_random_number':
        num_list = []
        for i in range(n):
            random_num = random.randint(0, 100)
            if random_num not in num_list:
                num_list.append(random_num)

        return tuple(num_list)
    if select_type == 'get_random_char':
        char_list = []
        for i in range(n):
            random_char = random.randint(65, 90)
            if chr(random_char) not in char_list:
                char_list.append(chr(random_char))
        return tuple(char_list)
    if select_type == 'matrix_product':
        print('-----------原始矩阵-----------')
        for i in range(n):
            for j in range(n):
                print('%-6d' % (n*i+j+1), end='')
            print('\n')
        print('-----------矩阵转置-----------')
        for i in range(n):
            for j in range(n):
                print('%-6d' % (n*j+i+1), end='')
            print('\n')


my_math = math_func('get_random_char', 16)
print(my_math)
my_math = math_func('get_random_number', 50)
print(my_math)
my_math = math_func('factorial', 5)
print(my_math)
my_math = math_func('cubic', 5)
print(my_math)
my_math = math_func('matrix_product', 5)

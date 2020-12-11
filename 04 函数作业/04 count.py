"""
文件说明
定义一个 ount_str_ char( my_ st1 ）函数，该函数返回参数字符串中包含多少个数字、 少个
英文字母、多少个空白字符、多少个其他字符
"""


def count_str_char(my_str):
    number_count = 0
    char_count = 0
    blank_char_count = 0
    other_char_count = 0
    for i in range(len(my_str)):
        # ord 获取字符的ascii码
        if 48 <= ord(my_str[i]) <= 57:
            number_count = number_count + 1
        elif 65 <= ord(my_str[i]) <= 90 or 97 <= ord(my_str[i]) <= 122:
            char_count = char_count + 1
        elif my_str[i] == ' ':
            blank_char_count = blank_char_count + 1
        else:
            other_char_count = other_char_count + 1

    print(number_count, char_count, blank_char_count, other_char_count)


count_str_char('sag54135d 5415s>sf')  # 9 7 1 1

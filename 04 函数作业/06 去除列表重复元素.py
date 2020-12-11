"""
文件说明

"""


def remove_duplicate_elements(data):
    output_list = []
    for i in range(len(data)):
        if data[i] not in output_list:
            output_list.append(data[i])
    return output_list


print(remove_duplicate_elements([2, 5, 6, 8, 2, 6, 4, 8, 6, 2]))

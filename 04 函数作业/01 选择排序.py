"""
文件说明
定义一个函数,该函数可接收一个 list 作为参数,该函数使用直接选择排序对 list排序

选择排序：
第一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，
然后再从剩余的未排序元素中寻找到最小（大）元素，然后放到已排序的序列的末尾。以此类推，直到全部待排序的数据元素的个数为零。
"""


def select_sorting(rec_list):
    for i in range(len(rec_list)-1):
        for j in range(i+1, len(rec_list)):
            # i 是开头第一个，j是遍历剩下所有的
            # 如果剩下的有比第一个小，那么就交换位置，
            if rec_list[j] < rec_list[i]:
                temp = rec_list[j]
                rec_list[j] = rec_list[i]
                rec_list[i] = temp
    print(rec_list)


select_sorting([1,5,3,6,8,45,62,15])
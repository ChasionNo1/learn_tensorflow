"""
文件说明
定义一个函数,该函数可接收一个 list 作为参数,该函数使用冒泡排序对 list排序

冒泡排序：
比较相邻的元素。如果第一个比第二个大，就交换他们两个。
对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
针对所有的元素重复以上的步骤，除了最后一个。
持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

"""


def bubbling_sort(rec_list):
    # n个数排序，确定n-1个后，剩下的一个也就确定了，外循环是n-1次
    # 内循环，每次前后两个比较，需要n-1次，随着确定位置后，剩下的位置等于n-i-1
    for i in range(len(rec_list)-1):
        for j in range(len(rec_list)-i-1):
            if rec_list[j] > rec_list[j+1]:
                # 可以这样直接交换
                rec_list[j], rec_list[j+1] = rec_list[j+1], rec_list[j]
    print(rec_list)


bubbling_sort([1, 5, 7, 6, 8, 45, 62, 15, 4, 13, 2])



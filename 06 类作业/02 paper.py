"""
文件说明
2．利用第1题定义的Student类，定义一个列表保存多个Student对象作为通讯录数据。程序
可通过name、email、address查询，如果找不到数据，则进行友好提示。
"""
from Student import Student
'''
('张三', 18, '男')
('李四', 19, '男')
('小红', 17, '女')
python导入另一个类的方法：from py文件名 import 要导入的类名
'''


def search(name):
    s1 = Student('张三', 18, '男')
    s2 = Student('李四', 19, '男')
    s3 = Student('小红', 17, '女')
    # 将student对象添加到列表中
    stu_list = [s1, s2, s3]
    flag = 0
    for stu in stu_list:
        if name == stu.name:
            flag = 1
            print('姓名：'+stu.name + ', 年龄：' + str(stu.age) + ', 性别：' + stu.gender)
            break
        else:
            flag = 0
    if flag == 0:
        print('未找到')


search('小红')

"""
文件说明
3．定义代表二维坐标系上某个点的Point类（包括x、y两个属性)，为该类提供一个方法用
于计算两个Point之间的距离，再提供一个方法用于判断三个Point组成的三角形是钝角、锐角还
是直角三角形。
"""
import sympy


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    # 计算两个的距离
    # 这里有一个问题，就是开方不是整数的话，保存会有损失，所以再次平方的话不等于原来的值
    # 导入sympy包，可以保留根号的形式
    def calculate_distance(cls, pointA, pointB):
        sympy.init_printing()
        # 将x和y用这两个符号暂时表示
        x, y = sympy.symbols('x y')
        # 给出表达式
        sympy.sqrt(x ** 2 + y ** 2)
        # 赋值，返回计算结果
        x = pointA.x - pointB.x
        y = pointA.y - pointB.y
        return sympy.sqrt(x**2 + y**2)

    @classmethod
    # 计算三个点组成的三角形是什么三角形？
    def jungle_rectangle(cls, pointA, pointB, pointC):
        # 得到三个边长
        ab = Point.calculate_distance(pointA, pointB)
        ac = Point.calculate_distance(pointA, pointC)
        bc = Point.calculate_distance(pointC, pointB)
        edge = [ab, ac, bc]
        print(edge)
        sorted_list = sorted(edge)
        # 最小的两条边平方和大于第三边是钝角，等于是直角，小于是锐角
        if sorted_list[0]**2 + sorted_list[1]**2 > sorted_list[2]**2:
            print('是钝角')
        elif sorted_list[0]**2 + sorted_list[1]**2 == sorted_list[2]**2:
            print('是直角')
        else:
            print('是锐角')


a = Point(0, 0)
b = Point(2, 1)
c = Point(0, 3)
Point.jungle_rectangle(a, b, c)


"""
文件说明
定义代表三维笛卡尔坐标系上某个点的point类（包括x，y，z三个属性），为该类定义一个方法，可接收
b，c，d三个参数，用于计算当前点、b、c组成的面与b、c、d组成的面之间的夹角。

"""
import sympy
import math


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    @staticmethod
    def calculate_angle(a, b, c, d):
        # 计算夹角，计算向量
        bc = Point.calculate_vector(b, c)
        ab = Point.calculate_vector(a, b)
        cd = Point.calculate_vector(c, d)
        print(bc, ab, cd)
        X = Point.cross_product(ab, bc)
        Y = Point.cross_product(bc, cd)
        cosXY = Point.dot_product(X, Y)/(Point.module_vector(X)*Point.module_vector(Y))
        angle = math.acos(cosXY)
        return angle

    @staticmethod
    def calculate_vector(x1, x2):
        # 计算两个点的向量,返回的是元组
        return x1.x-x2.x, x1.y-x2.y, x1.z-x2.z

    @staticmethod
    def dot_product(x1, x2):
        # 计算两个向量的点乘
        return x1[0]*x2[0] + x1[1]*x2[1] + x1[2]*x2[2]

    @staticmethod
    def cross_product(x1, x2):
        # 计算两个向量叉乘， （y1z2-z1y2,x2z1-x1z2,x1y2-y1x2）
        x11 = x1[0]
        y1 = x1[1]
        z1 = x1[2]
        x22 = x2[0]
        y2 = x2[1]
        z2 = x2[2]
        return y1*z2-z1*y2, x22*z1-x11*z2, x11*y2-y1*x22

    @staticmethod
    def module_vector(v):
        sympy.init_printing()
        x, y, z = sympy.symbols('x y z')
        sympy.sqrt(x ** 2 + y ** 2 + z**2)
        x = v[0]
        y = v[1]
        z = v[2]
        return sympy.sqrt(x ** 2 + y ** 2 + z**2)


a = Point(1, 2, 3)
b = Point(2, 2, 6)
c = Point(3, 5, 3)
d = Point(9, 2, 6)
print(Point.calculate_angle(a, b, c, d))



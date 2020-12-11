"""
文件说明

"""


class Canvas:
    def draw_pic(self, shape):
        print('----开始绘图-----')
        shape.draw(self)


class Rectangle:
    def draw(self, canvas):
        print('在%s上绘制矩形' % canvas)


class Triangle:
    def draw(self, canvas):
        print('在%s上绘制三角形' % canvas)


class Circle:
    def draw(self, canvas):
        print('在%s上绘制圆形' % canvas)


c = Canvas()
# Rectangle--->shape
# Rectangle.draw----->shape.draw
# shape.draw(self)：self参数代表canvas
c.draw_pic(Rectangle())
c.draw_pic(Triangle())
c.draw_pic(Circle())

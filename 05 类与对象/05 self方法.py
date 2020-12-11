"""
文件说明

"""


class ReturnSelf:
    def grow(self):
        if hasattr(self, 'age'):
            self.age += 1
        else:
            self.age = 1
        return self


rs = ReturnSelf()
rs.grow().grow().grow()
print('rs的age属性值是：', rs.age)

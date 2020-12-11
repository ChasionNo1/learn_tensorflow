"""
文件说明

"""


class Cell:
    # 使用@property修饰方法，相当于为该属性设置getter方法
    @property
    def state(self):
        return self._state
    # 为state属性设置setter方法
    @state.setter
    def state(self, value):
        if 'alive' in value.lower():
            self._state = 'alive'
        else:
            self._state = 'dead'

    @property
    def is_dead(self):
        return not self._state.lower() == 'alive'


c = Cell()
c.state = 'Alive'
print(c.state)
print(c.is_dead)

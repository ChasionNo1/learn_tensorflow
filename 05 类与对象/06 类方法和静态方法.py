"""
文件说明

"""


class Bird:
    @classmethod
    def fly(cls):
        print('类方法fly：', cls)

    @staticmethod
    def info(p):
        print('静态方法info：', p)


# 调用类方法，Bird类会自动绑定到第一个参数
Bird.fly()
# 调用静态方法，不会自动绑定，因此程序必须手动绑定第一个参数
Bird.info('adsf')
# 创建Bird对象
b = Bird()
# 使用对象调用fly类方法，其实依然还是使用类调用的
b.fly()
# 使用对象调用info静态方法，其实依然还是使用类调用的
# 因此程序必须为第一个参数执行绑定
b.info('sdsdsd')


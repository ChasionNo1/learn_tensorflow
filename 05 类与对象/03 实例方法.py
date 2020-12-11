"""
文件说明

"""


class Dog:
    def jump(self):
        print('正在执行jump方法')

    def run(self):
        # 谁调用run方法，那么self就代表谁，当Dog对象调用run方法时，run方法需要依赖jump方法
        # python对象的一个方法调用另一个方法时，不可以省略self。
        self.jump()
        print('正在执行run方法')


dog = Dog()
dog.run()
# 正在执行jump方法
# 正在执行run方法
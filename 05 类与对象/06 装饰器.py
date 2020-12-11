"""
文件说明

"""


def funA(fn):
    print('a')
    fn()
    return 'b'


@funA
def funB():
    print('B')


print(funB)
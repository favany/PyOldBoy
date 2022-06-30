"""
@Time    : 2022/6/30 10:49
@Author  : 刘俊 jun.liu@deepfinance.com
@File    : 01 叠加多个装饰器分析.py
"""

'''
一、叠加多个装饰器的加载、运行分析（了解 ***）
'''


def deco1(func1):  # func1 = 被装饰对象 wrapper2 的内存地址
    def wrapper1(*args, **kwargs):
        print('正在运行：deco1.wrapper1')
        res1 = func1(*args, **kwargs)
        return res1
    return wrapper1


def deco2(func2):  # func2 = 被装饰对象 wrapper3 的内存地址
    def wrapper2(*args, **kwargs):
        print('正在运行：deco2.wrapper2')
        res2 = func2(*args, **kwargs)
        return res2
    return wrapper2


def deco3(x):
    def outer(func3):  # func3 = 被装饰对象 index 函数的内存地址
        def wrapper3(*args, **kwargs):
            print('正在运行：deco3.outer.wrapper3')
            res3 = func3(*args, **kwargs)
            return res3
        return wrapper3
    return outer


@deco1       # index = deco1(wrapper2 的内存地址) => index = wrapper1 的内存地址
@deco2       # index = deco2(wrapper3 的内存地址) => index = wrapper2 的内存地址
@deco3('1')  # @outer3 => index = outer3(index) => index = wrapper3 的内存地址
def index(x, y):
    print('from index %s:%s' % (x, y))


'''
加载顺序：自下而上
'''
# print(index)  # <function deco1.<locals>.wrapper1 at 0x102f39700>  （运行顺序：wrapper3 => wrapper2 => wrapper1）

'''
执行顺序：自下而上

'''

index(1, 2)

'''
正在运行：deco1.wrapper1
正在运行：deco2.wrapper2
正在运行：deco3.outer.wrapper3
from index 1:2
'''


# @File      : 01 无参装饰器
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/6/19 9:07 AM
# @Info      :

"""
装饰器
1. 什么是装饰器
 器是指工具，可以定义成函数；装饰是指添加额外的功能。
 装饰器指的是定义一个函数，该函数是用来为其他函数增加功能的。

2. 为何要用装饰器
 开放封闭原则
 开放 指的是对拓展功能是开放的
 封闭 指的是对修改源代码是封闭的

3. 如何用




"""

"""
一、储备知识
1. *args **kwargs
def index(x, y):
    print(x, y)

def wrapper(*args, **kwargs):
    index(*args, **kwargs)  # index(y=222, x=111)

wrapper(y=222, x=111)

2. 名称空间与作用域：名称空间的"嵌套"关系是在函数定义阶段，即检测语法的时候确定的


3. 函数对象：
   可以把函数当作参数传入
   可以把函数当作返回值返回


4. 函数的嵌套定义
def outter(func):
    def wrapper():
        ...
    return wrapper


5. 闭包函数
def outter():
    x = 111
    def wrapper():
        x
    return wrapper

f = outter()

传参的方式：
（一）通过参数的形式为函数体传值

def func(x):
    x

（二）通过闭包的方式为函数体传值

def outter(x):
    def wrapper():
        print(x)
    return wrapper

二、装饰器
1. 什么是装饰器？
    器指的是工具，可以定义成函数
    装饰指的是为其他食物添加额外的东西点缀

    合到一起的解释：
        装饰器指的是定义一个函数，该函数是用来为其他函数增加功能的。

2. 为何要用装饰器
    开放封闭原则
        开放：对拓展功能是开放的
        封闭：对修改源代码是封闭的

    装饰器就是在不修改被装饰器对象源代码，以及调用方式的前提下，为被装饰对象添加新功能
"""


# 需求：在不修改 index 函数的源代码以及调用方式的前提下，为其添加统计运行时间的功能

# def index(x, y):
#     time.sleep(3)
#     print('index %s %s' % (x, y))
#
#
# index(1, 2)
# index(3, 4)
# index(5, 6)

# 解决方案一：失败
# 问题： 没有修改被装饰对象的调用方式，但是修改了其源代码
# import time
#
#
# def index(x, y):
#     start = time.time()
#     time.sleep(3)
#     print('index %s %s' % (x, y))
#     stop = time.time()
#     print(stop - start)


# index(1, 2)
# index(3, 4)
# index(5, 6)

# 解决方案二
# 问题：没有修改被装饰对象的调用方式，也没有修改其源代码，并且加上了新功能
#      但是代码冗余
# import time
#
#
# def index(x, y):
#     time.sleep(3)
#     print('index %s %s' % (x, y))
#
#
# start = time.time()
# index(1, 2)
# stop = time.time()
# print(stop - start)
#
#
# start = time.time()
# index(1, 2)
# stop = time.time()
# print(stop - start)
#
#
# start = time.time()
# index(1, 2)
# stop = time.time()
# print(stop - start)



# 解决方案三
# 问题：解决了方案二的代码冗余问题，但带来一个新问题。即函数的调用方式改了。
# import time
#
#
# def index(x, y):
#     time.sleep(3)
#     print('index %s %s' % (x, y))
#
#
# def wrapper(*args, **kwargs):
#     start = time.time()
#     index(*args, **kwargs)
#     stop = time.time()
#     print(stop - start)
#
# wrapper(3, 4)


# 解决方案四：如何在方案三的基础上，不改变函数的调用方式
import time


def index(x, y):
    time.sleep(3)
    print('index %s %s' % (x, y))

def outter(func):
    # func = index
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        stop = time.time()
        print(stop - start)
    return wrapper

# f = outter(index)  # f= wrapper 函数的内存地址， index 是index 函数的内存地址
#
# f(x=1, y=2)

index = outter(index)
index(x=1, y=2)





# 07 -

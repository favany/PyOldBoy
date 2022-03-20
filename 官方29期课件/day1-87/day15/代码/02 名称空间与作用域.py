"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""

# 一：名称空间namespacs：存放名字的地方，是对栈区的划分
# 有了名称空间之后，就可以在栈区中存放相同的名字，详细的，名称空间
# 分为三种
# 1.1 内置名称空间
# 存放的名字：存放的python解释器内置的名字
'''
>>> print
<built-in function print>
>>> input
<built-in function input>
'''
# 存活周期：python解释器启动则产生，python解释器关闭则销毁


# 1.2 全局名称空间
# 存放的名字：只要不是函数内定义、也不是内置的，剩下的都是全局名称空间的名字
# 存活周期：python文件执行则产生，python文件运行完毕后销毁

# import os
#
# x=10
# if 13 > 3:
#     y=20
#     if 3 == 3:
#         z=30
#
# # func=函数的内存地址
# def func():
#     a=111
#     b=222

# class Foo:
#     pass



# 1.3 局部名称空间
# 存放的名字：在调用函数时，运行函数体代码过程中产生的函数内的名字
# 存活周期：在调用函数时存活，函数调用完毕后则销毁
# def func(a,b):
#     pass
#
# func(10,1)
# func(11,12)
# func(13,14)
# func(15,16)


# 1.4 名称空间的加载顺序
# 内置名称空间>全局名称空间>局部名称空间

# 1.5 销毁顺序
# 局部名称空间>全局名空间>内置名称空间

# 1.6 名字的查找优先级：当前所在的位置向上一层一层查找
# 内置名称空间
# 全局名称空间
# 局部名称空间

# 如果当前在局部名称空间：
# 局部名称空间—>全局名称空间->内置名称空间
# # input=333
#
# def func():
#     # input=444
#     print(input)
#
# func()


# 如果当前在全局名称空间
# 全局名称空间->内置名称空间
# input=333
# def func():
#     input=444
# func()
# print(input)


# 示范1:
# def func():
#     print(x)
# x=111
#
# func()

# 示范2：名称空间的"嵌套"关系是以函数定义阶段为准，与调用位置无关
# x=1
# def func():
#    print(x)
#
#
# def foo():
#     x=222
#     func()
#
# foo()

# 示范3：函数嵌套定义
# input=111
# def f1():
#     def f2():
#         # input=333
#         print(input)
#     input=222
#
#     f2()
#
#
# f1()


# 示范4：
# x=111
# def func():
#     print(x) #
#     x=222
#
# func()


# 二：作用域-》作用范围
# 全局作用域：内置名称空间、全局名称空间
# 1、全局存活
# 2、全局有效:被所有函数共享

# x=111
#
# def foo():
#     print(x,id(x))
#
# def bar():
#     print(x,id(x))
#
# foo()
# bar()

# print(x,id(x))

# 局部作用域: 局部名称空间的名字
# 1、临时存活
# 2、局部有效:函数内有效

# def foo(x):
#     def f1():
#         def f2():
#             print(x)



# LEGB
# # builtin
# # global
# def f1():
#     # enclosing
#     def f2():
#         # enclosing
#         def f3():
#             # local
#             pass















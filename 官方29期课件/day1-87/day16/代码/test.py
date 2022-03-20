"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""


# x=10
# def func():
#     global x
#     x=20
#
# func()
# print(x)


# l=[1,2]
# def func():
#     # global l
#     # l=123
#     l.append(3)
#
# func()
# print(l)

# def func():
#     global x
#     x=111
#
# func()
# print(x)








# def f1():
#     x=1
#     def f2():
#         nonlocal x
#         x=2






# # ===================题目一===================
# input=333
# def func():
#     input=444
#     print(input)
#
# func()
# print(input)

# # ===================题目二===================
# def func():
#     print(x)
# x=111
#
# func()


# # ===================题目三===================
# x=1
# def func():
#    print(x)
#
#
# def foo():
#     x=222
#     func()
#
# x=333
#
#
# foo()
#
# # ===================题目四===================
# input=111
# def f1():
#     def f2():
#         # input=333
#         print(input)
#     # input=222
#     f2()
# input=333
#
# f1()


#
# # ===================题目五===================
# x=111
# def func():
#     print(x) #
#     x=222
#
# func()
#
#
# # ===================题目六===================
# x=111
#
# def foo():
#     print(x,)
#
# def bar():
#     print(x)
#
# foo()
# bar()
#
# # ===================题目七===================
# x=1
# def func2():
#     func1()
#
# x=2
# def func1():
#     print(x)
#
# x=3
#
# func2()


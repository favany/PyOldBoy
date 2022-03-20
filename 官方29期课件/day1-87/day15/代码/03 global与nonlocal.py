"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""
# 示范1：
# x=111
#
# def func():
#     x=222
#
# func()
# print(x)

# 示范2：如果再局部想要修改全局的名字对应的值（不可变类型），需要用global
# x=111
#
# def func():
#     global x # 声明x这个名字是全局的名字，不要再造新的名字了
#     x=222
#
# func()
# print(x)


# 示范3：
# l=[111,222]
# def func():
#     l.append(333)
#
# func()
# print(l)


# nonlocal(了解): 修改函数外层函数包含的名字对应的值（不可变类型）
# x=0
# def f1():
#     x=11
#     def f2():
#         nonlocal x
#         x=22
#     f2()
#     print('f1内的x：',x)
#
# f1()



def f1():
    x=[]
    def f2():
        x.append(1111)
    f2()
    print('f1内的x：',x)

f1()


























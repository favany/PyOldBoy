"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""
# 函数嵌套
# 1、函数的嵌套调用：在调用一个函数的过程中又调用其他函数
# def max2(x,y):
#     if x > y:
#         return x
#     else:
#         return y
#
#
# def max4(a,b,c,d):
#     # 第一步：比较a，b得到res1
#     res1=max2(a,b)
#     # 第二步：比较res1，c得到res2
#     res2=max2(res1,c)
#     # 第三步：比较res2，d得到res3
#     res3=max2(res2,d)
#     return res3
#
# res=max4(1,2,3,4)
# print(res)


# 2、函数的嵌套定义:在函数内定义其他函数
# def f1():
#     def f2():
#         pass


# 圆形
# 求圆形的求周长：2*pi*radius
def circle(radius,action=0):
    from math import pi

    def perimiter(radius):
        return 2*pi*radius

    # 求圆形的求面积：pi*(radius**2)
    def area(radius):
        return pi*(radius**2)

    if action == 0:
        return 2*pi*radius

    elif action == 1:
        return area(radius)

circle(33,action=0)


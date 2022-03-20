"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""


# impot导入模块在使用时必须加前缀"模块."
# 优点：肯定不会与当前名称空间中的名字冲突
# 缺点：加前缀显得麻烦

# from ... import ...导入也发生了三件事
# 1、产一个模块的名称空间
# 2、运行foo.py将运行过程中产生的名字都丢到模块的名称空间去
# 3、在当前名称空间拿到一个名字，该名字与模块名称空间中的某一个内存地址
# from foo import x # x=模块foo中值0的内存地址
# from foo import get
# from foo import change

# print(x)
# print(get)
# print(change)
# x=333333333
# print(x)
# get()
# change()
# get()

# print(x)
# from foo import x # x=新地址
# print(x)

# from...impot...导入模块在使用时不用加前缀
# 优点：代码更精简
# 缺点：容易与当前名称空间混淆
# from foo import x # x=模块foo中值1的内存地址
# x=1111


# 一行导入多个名字(不推荐)
# from foo import x,get,change

# *：导入模块中的所有名字
# name='egon'
# from foo import *
# print(name)

from socket import *


# 了解：__all__
# from foo import *
# print(x)
# print(get)
# print(change)


# 起别名
from foo import get as g
print(g)



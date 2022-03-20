"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""


# 一：封装介绍
# 封装是面向对象三大特性最核心的一个特性
# 封装<->整合


# 二、将封装的属性进行隐藏操作
# 1、如何隐藏：在属性名前加__前缀,就会实现一个对外隐藏属性效果
# 该隐藏需要注意的问题：
# I:在类外部无法直接访问双下滑线开头的属性，但知道了类名和属性名就可以拼出名字：_类名__属性，然后就可以访问了，如Foo._A__N，
# 所以说这种操作并没有严格意义上地限制外部访问，仅仅只是一种语法意义上的变形。
# class Foo:
#     __x = 1  # _Foo__x
#
#     def __f1(self):  # _Foo__f1
#         print('from test')
#
#
# # print(Foo.__dict__)
# # print(Foo._Foo__x)
# # print(Foo._Foo__f1)

# II：这种隐藏对外不对内,因为__开头的属性会在检查类体代码语法时统一发生变形
# class Foo:
#     __x = 1  # _Foo__x = 1
#
#     def __f1(self):  # _Foo__f1
#         print('from test')
#
#     def f2(self):
#         print(self.__x) # print(self._Foo__x)
#         print(self.__f1) # print(self._Foo__f1)

# print(Foo.__x)
# print(Foo.__f1)
# obj=Foo()
# obj.f2()

# III: 这种变形操作只在检查类体语法的时候发生一次，之后定义的__开头的属性都不会变形
# class Foo:
#     __x = 1  # _Foo__x = 1
#
#     def __f1(self):  # _Foo__f1
#         print('from test')
#
#     def f2(self):
#         print(self.__x) # print(self._Foo__x)
#         print(self.__f1) # print(self._Foo__f1)
#
# Foo.__y=3
# print(Foo.__dict__)
# print(Foo.__y)

# class Foo:
#     __x = 1  # _Foo__x = 1
#
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#
# obj=Foo('egon',18)
# print(obj.__dict__)
# print(obj.name,obj.age)

# 2、为何要隐藏？
# I、隐藏数据属性"将数据隐藏起来就限制了类外部对数据的直接操作，然后类内应该提供相应的接口来允许类外部间接地操作数据，接口之上可以附加额外的逻辑来对数据的操作进行严格地控制：
# 设计者：egon
class People:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        # 通过该接口就可以间接地访问到名字属性
        # print('小垃圾，不让看')
        print(self.__name)

    def set_name(self,val):
        if type(val) is not str:
            print('小垃圾，必须传字符串类型')
            return
        self.__name=val

# 使用者：王鹏
obj = People('egon')
# print(obj.name) # 无法直接用名字属性
# obj.set_name('EGON')
obj.set_name(123123123)
obj.get_name()
# II、隐藏函数/方法属性：目的的是为了隔离复杂度


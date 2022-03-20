"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""
# 单继承背景下的属性查找
# 示范一：
# class Foo:
#     def f1(self):
#         print('Foo.f1')
#
#     def f2(self):
#         print('Foo.f2')
#         self.f1() # obj.f1()
#
# class Bar(Foo):
#     def f1(self):
#         print('Bar.f1')
#
# obj=Bar()
# obj.f2()
#
# # Foo.f2
# # Foo.f1



# # 示范二：
# class Foo:
#     def f1(self):
#         print('Foo.f1')
#
#     def f2(self):
#         print('Foo.f2')
#         Foo.f1(self) # 调用当前类中的f1
#
# class Bar(Foo):
#     def f1(self):
#         print('Bar.f1')
#
# obj=Bar()
# obj.f2()
#
# # Foo.f2
# # Foo.f1

# 示范三：
class Foo:
    def __f1(self): # _Foo__f1
        print('Foo.f1')

    def f2(self):
        print('Foo.f2')
        self.__f1() # self._Foo__f1,# 调用当前类中的f1

class Bar(Foo):
    def __f1(self): # _Bar__f1
        print('Bar.f1')

obj=Bar()
obj.f2()

# Foo.f2
# Foo.f1





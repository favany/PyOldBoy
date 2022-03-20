#coding:utf-8
"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""
# 一：菱形问题介绍与MRO
# class A(object):
#     # def test(self):
#     #     print('from A')
#     pass
#
# class B(A):
#     def test(self):
#         print('from B')
#     pass
#
# class C(A):
#     # def test(self):
#     #     print('from C')
#     pass
#
# class D(C,B):
#     # def test(self):
#     #     print('from D')
#     pass
#
# print(D.mro()) # 类D以及类D的对象访问属性都是参照该类的mro列表
#
# # obj = D()
# # obj.test()
#
# # print(D.test)
#
# # print(C.mro()) # 类C以及类C的对象访问属性都是参照该类的mro列表
# # c=C()
# # c.test()
#
# # 总结：类相关的属性查找（类名.属性，该类的对象.属性），都是参照该类的mro


# # 二：如果多继承是非菱形继承，经典类与新式的属性查找顺序一样：
# #    都是一个分支一个分支地找下去，然后最后找object
# class E:
#     # def test(self):
#     #     print('from E')
#     pass
#
# class F:
#     def test(self):
#         print('from F')
#
#
# class B(E):
#     # def test(self):
#     #     print('from B')
#     pass
#
# class C(F):
#     # def test(self):
#     #     print('from C')
#     pass
#
# class D:
#     def test(self):
#         print('from D')
#
#
# class A(B, C, D):
#     # def test(self):
#     #     print('from A')
#     pass
#
# # 新式类
# # print(A.mro()) # A->B->E->C->F->D->object
#
# obj = A()
# obj.test() # 结果为：from F


# 三：如果多继承是菱形继承，经典类与新式类的属性查找顺序不一样：
#    经典类：深度优先，会在检索第一条分支的时候就直接一条道走到黑，即会检索大脑袋（共同的父类）
#    新式类：广度优先，会在检索最后一条分支的时候检索大脑袋
class G: # 在python2中，未继承object的类及其子类，都是经典类
    # def test(self):
    #     print('from G')
    pass

class E(G):
    # def test(self):
    #     print('from E')
    pass

class F(G):
    def test(self):
        print('from F')

class B(E):
    # def test(self):
    #     print('from B')
    pass

class C(F):
    def test(self):
        print('from C')

class D(G):
    def test(self):
        print('from D')

class A(B,C,D):
    # def test(self):
    #     print('from A')
    pass

# 新式类
# print(A.mro()) # A->B->E->C->F->D->G->object

# 经典类：A->B->E->G->C->F->D
obj = A()
obj.test() #


# 总结：
# 多继承到底要不用？？？
# 要用，但是规避几点问题
# 1、继承结构尽量不要过于复杂
# 2、推荐使用mixins机制：在多继承的背景下满足继承的什么"是"什么的关系













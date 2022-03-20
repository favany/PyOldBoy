"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""
# 1、什么多态：同一事物有多种形态
# class Animal:
#     pass
#
# class People(Animal):
#     pass
#
# class Dog(Animal):
#     pass
#
# class Pig(Animal):
#     pass


# 2、为何要有多态=》多态会带来什么样的特性，多态性
#    多态性指的是可以在不考虑对象具体类型的情况下而直接使用对象
# class Animal: # 统一所有子类的方法
#     def say(self):
#         print('动物基本的发声频率。。。',end=' ')
#
# class People(Animal):
#     def say(self):
#         super().say()
#         print('嘤嘤嘤嘤嘤嘤嘤')
#
# class Dog(Animal):
#     def say(self):
#         super().say()
#         print('汪汪汪')
#
# class Pig(Animal):
#     def say(self):
#         super().say()
#         print('哼哼哼')
#
#
# obj1=People()
# obj2=Dog()
# obj3=Pig()

#
# obj1.say()
# obj2.say()
# obj3.say()

# 定义统一的接口，接收传入的动物对象
# def animal_say(animal):
#     animal.say()
#
# animal_say(obj1)
# animal_say(obj2)
# animal_say(obj3)


# print('hello'.__len__())
# print([1,2,3].__len__())
# print({'a':1,'b':2}.__len__())
#
# def my_len(val):
#     return val.__len__()

# print(my_len('hello'))
# print(my_len([1,2,3]))
# print(my_len({'a':1,'b':2}))

# len('hello')
# len([1,2,3])
# len({'a':1,'b':2})


# python推崇的是鸭子类型
# class Cpu:
#     def read(self):
#         print('cpu read')
#
#     def write(self):
#         print('cpu write')
#
# class Mem:
#     def read(self):
#         print('mem read')
#
#     def write(self):
#         print('mem write')
#
#
# class Txt:
#     def read(self):
#         print('txt read')
#
#     def write(self):
#         print('txt write')
#
#
# obj1=Cpu()
# obj2=Mem()
# obj3=Txt()
#
# obj1.read()
# obj1.write()
#
# obj2.read()
# obj2.write()
#
# obj3.read()
# obj3.write()


# 了解：
import abc

class Animal(metaclass=abc.ABCMeta): # 统一所有子类的标准
    @abc.abstractmethod
    def say(self):
        pass

# obj=Animal() # 不能实例化抽象类自己

class People(Animal):
    def say(self):
        pass

class Dog(Animal):
    def say(self):
        pass

class Pig(Animal):
    def say(self):
        pass

#
# obj1=People()
# obj2=Dog()
# obj3=Pig()


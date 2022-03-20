"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""

# 装饰器是在不修改被装饰对象源代码以及调用方式的前提下为被装饰对象添加
# 新功能的可调用对象
# print(property)

# property是一个装饰器，是用来绑定给对象的方法伪造成一个数据属性


"""
成人的BMI数值：
过轻：低于18.5
正常：18.5-23.9
过重：24-27
肥胖：28-32
非常肥胖, 高于32
　　体质指数（BMI）=体重（kg）÷身高^2（m）
　　EX：70kg÷（1.75×1.75）=22.86
"""


# 案例一：

# class People:
#     def __init__(self, name, weight, height):
#         self.name = name
#         self.weight = weight
#         self.height = height
#
#     # 定义函数的原因1：
#     # 1、从bmi的公式上看，bmi应该是触发功能计算得到的
#     # 2、bmi是随着身高、体重的变化而动态变化的，不是一个固定的值
#     #    说白了，每次都是需要临时计算得到的
#
#     # 但是bmi听起来更像是一个数据属性，而非功能
#     @property
#     def bmi(self):
#         return self.weight / (self.height ** 2)


# obj1 = People('egon', 70, 1.83)
# print(obj1.bmi())

# obj1.height=1.86
# print(obj1.bmi())

# print(obj1.bmi)

# # 案例二：
# class People:
#     def __init__(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, val):
#         if type(val) is not str:
#             print('必须传入str类型')
#             return
#         self.__name = val
#
#     def del_name(self):
#         print('不让删除')
#         # del self.__name
#
#     name=property(get_name,set_name,del_name)
#
# obj1=People('egon')
# # print(obj1.get_name())
# # obj1.set_name('EGON')
# # print(obj1.get_name())
# # obj1.del_name()
#
#
#
# # 人正常的思维逻辑
# print(obj1.name) #
# # obj1.name=18
# # del obj1.name



# 案例三：
class People:
    def __init__(self, name):
        self.__name = name


    @property
    def name(self): # obj1.name
        return self.__name

    @name.setter
    def name(self, val): # obj1.name='EGON'
        if type(val) is not str:
            print('必须传入str类型')
            return
        self.__name = val

    @name.deleter
    def name(self): # del obj1.name
        print('不让删除')
        # del self.__name


obj1=People('egon')
# 人正常的思维逻辑
print(obj1.name) #
# obj1.name=18
# del obj1.name















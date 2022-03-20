"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""

# 多继承的正确打开方式：mixins机制
# mixins机制核心：就是在多继承背景下尽可能地提升多继承的可读性
# ps：让多继承满足人的思维习惯=》什么"是"什么
class Vehicle:
    pass

class FlyableMixin:
    def fly(self):
        pass

class CivilAircraft(FlyableMixin,Vehicle):  # 民航飞机
    pass

class Helicopter(FlyableMixin,Vehicle):  # 直升飞机
    pass

class Car(Vehicle):  # 汽车并不会飞，但按照上述继承关系，汽车也能飞了
    pass


import socketserver
# 补充：通常Mixin结果的类放在左边
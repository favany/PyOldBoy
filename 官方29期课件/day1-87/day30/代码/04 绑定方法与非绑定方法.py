"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""
# 一：绑定方法：特殊之处在于将调用者本身当做第一个参数自动传入
#    1、绑定给对象的方法：调用者是对象，自动传入的是对象
#    2、绑定给类的方法：调用者类，自动传入的是类
# import settings
#
# class Mysql:
#     def __init__(self,ip,port):
#         self.ip=ip
#         self.port=port
#
#     def func(self):
#         print('%s:%s' %(self.ip,self.port))
#
#     @classmethod # 将下面的函数装饰成绑定给类的方法
#     def from_conf(cls):
#         print(cls)
#         return cls(settings.IP, settings.PORT)
#
# # obj1=Mysql('1.1.1.1',3306)
#
# obj2=Mysql.from_conf()
# print(obj2.__dict__)

# 二：非绑定方法-》静态方法：
#    没有绑定给任何人：调用者可以是类、对象，没有自动传参的效果

class Mysql:
    def __init__(self,ip,port):
        self.nid=self.create_id()
        self.ip=ip
        self.port=port

    @staticmethod # 将下述函数装饰成一个静态方法
    def create_id():
        import uuid
        return uuid.uuid4()

    @classmethod
    def f1(cls):
        pass

    def f2(self):
        pass
obj1=Mysql('1.1.1.1',3306)

# print(Mysql.create_id)
# print(obj1.create_id)

# Mysql.create_id(1,2,3)
# obj1.create_id(4,5,6)

print(Mysql.create_id)
print(Mysql.f1)
print(obj1.f2)
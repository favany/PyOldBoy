"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""


# 1、什么是内置方法？
# 定义在类内部，以__开头并以__结果的方法
# 特点：会在某种情况下自动触发执行

# 2、为何要用内置方法？
# 为了定制化我们的类or对象

# 3、如何使用内置方法
# __str__:在打印对象时会自动触发，然后将返回值（必须是字符串类型）当做本次打印的结果输出
# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         # print('运行了...')
#         return "<%s:%s>" %(self.name,self.age)
#
#
# obj = People('辣白菜同学', 18)
#
# # print(obj.__str__())
# print(obj)  # <'辣白菜同学':18>
#
# # obj1=int(10)
# # print(obj1)

# __del__：在清理对象时触发，会先执行该方法
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.x = open('a.txt',mode='w')
        # self.x = 占据的是操作系统资源

    def __del__(self):
        # print('run...')
        # 发起系统调用，告诉操作系统回收相关的系统资源
        self.x.close()

obj = People('辣白菜同学', 18)
# del obj # obj.__del__()
print('============>')




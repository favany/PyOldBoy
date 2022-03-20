"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""
# 一：储备知识
#1、 *args， **kwargs
# def index(x,y):
#     print(x,y)
#
#
# def wrapper(*args,**kwargs):
#     index(*args,**kwargs) #
#                           # index(y=222,x=111)
# wrapper(y=222,x=111)


# 2、名称空间与作用域：名称空间的的"嵌套"关系是在函数定义阶段，即检测语法的时候确定的

# 3、函数对象：
#    可以把函数当做参数传入
#    可以把函数当做返回值返回
# def index():
#     return 123
#
# def foo(func):
#     return func
#
# foo(index)

# 4、函数的嵌套定义:
# def outter(func):
#     def wrapper():
#         pass
#     return wrapper


# 闭包函数
# def outter():
#     x=111
#     def wrapper():
#         x
#     return wrapper
#
# f=outter()



# 传参的方式一：通过参数的形式为函数体传值


# def wrapper(x):
#     print(1)
#     print(2)
#     print(3)
#     x
#
# wrapper(1)
# wrapper(2)
# wrapper(3)
# 传参的方式二：通过闭包的方式为函数体传值
# def outter(x):
#     # x=1
#     def wrapper():
#         print(1)
#         print(2)
#         print(3)
#         x
#     return wrapper # return outter内的wrapper那个函数的内地址
#
# # f1=outter(1)
# # f2=outter(2)
# # f3=outter(3)
#
#
# wrapper=outter(1)
#


#二 装饰器
"""
1、什么是装饰器
    器指的是工具，可以定义成成函数
    装饰指的是为其他事物添加额外的东西点缀
    
    合到一起的解释：
        装饰器指的定义一个函数，该函数是用来为其他函数添加额外的功能
        
    
2、为何要用装饰器
    开放封闭原则
        开放：指的是对拓展功能是开放的
        封闭：指的是对修改源代码是封闭的
        
    装饰器就是在不修改被装饰器对象源代码以及调用方式的前提下为被装饰对象添加新功能
3、如何用
"""
# 需求：在不修改index函数的源代码以及调用方式的前提下为其添加统计运行时间的功能
# def index(x,y):
#     time.sleep(3)
#     print('index %s %s' %(x,y))
#
# index(111,222)
# # index(y=111,x=222)
# # index(111,y=222)

# 解决方案一：失败
# 问题：没有修改被装饰对象的调用方式，但是修改了其源代码
# import time
#
# def index(x,y):
#     start=time.time()
#     time.sleep(3)
#     print('index %s %s' %(x,y))
#     stop = time.time()
#     print(stop - start)
#
# index(111,222)


# 解决方案二：失败
# 问题：没有修改被装饰对象的调用方式，也没有修改了其源代码，并且加上了新功能
#      但是代码冗余
# import time
#
# def index(x,y):
#     time.sleep(3)
#     print('index %s %s' %(x,y))
#
# start=time.time()
# index(111,222)
# stop=time.time()
# print(stop - start)
#
#
#
# start=time.time()
# index(111,222)
# stop=time.time()
# print(stop - start)
#
#
# start=time.time()
# index(111,222)
# stop=time.time()
# print(stop - start)


# 解决方案三：失败
# 问题：解决了方案二代码冗余问题，但带来一个新问题即函数的调用方式改变了
# import time
#
# def index(x,y):
#     time.sleep(3)
#     print('index %s %s' %(x,y))
#
# def wrapper():
#     start=time.time()
#     index(111,222)
#     stop=time.time()
#     print(stop - start)
#
# wrapper()

# 方案三的优化一：将index的参数写活了
# import time
#
# def index(x,y,z):
#     time.sleep(3)
#     print('index %s %s %s' %(x,y,z))
#
# def wrapper(*args,**kwargs):
#     start=time.time()
#     index(*args,**kwargs) # index(3333,z=5555,y=44444)
#     stop=time.time()
#     print(stop - start)
#
# # wrapper(3333,4444,5555)
# # wrapper(3333,z=5555,y=44444)


# 方案三的优化二：在优化一的基础上把被装饰对象写活了，原来只能装饰index
# import time
#
# def index(x,y,z):
#     time.sleep(3)
#     print('index %s %s %s' %(x,y,z))
#
# def home(name):
#     time.sleep(2)
#     print('welcome %s to home page' %name)
#
#
# def outter(func):
#     # func = index的内存地址
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         func(*args,**kwargs) # index的内存地址()
#         stop=time.time()
#         print(stop - start)
#     return wrapper
#
# index=outter(index) # index=wrapper的内存地址
# home=outter(home) # home=wrapper的内存地址
#
#
# home('egon')
# # home(name='egon')

# 方案三的优化三：将wrapper做的跟被装饰对象一模一样，以假乱真
# import time
#
# def index(x,y,z):
#     time.sleep(3)
#     print('index %s %s %s' %(x,y,z))
#
# def home(name):
#     time.sleep(2)
#     print('welcome %s to home page' %name)
#
# def outter(func):
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         res=func(*args,**kwargs)
#         stop=time.time()
#         print(stop - start)
#         return res
#
#
#
#     return wrapper
# # 偷梁换柱：home这个名字指向的wrapper函数的内存地址
# home=outter(home)
#
#
# res=home('egon') # res=wrapper('egon')
# print('返回值--》',res)

# 大方向：如何在方案三的基础上不改变函数的调用方式




# 语法糖：让你开心的语法
import time

# 装饰器
# def timmer(func):
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         res=func(*args,**kwargs)
#         stop=time.time()
#         print(stop - start)
#         return res
#
#
#
#     return wrapper
#
#
# # 在被装饰对象正上方的单独一行写@装饰器名字
# # @timmer # index=timmer(index)
# def index(x,y,z):
#     time.sleep(3)
#     print('index %s %s %s' %(x,y,z))
#
# # @timmer # home=timmer(ome)
# def home(name):
#     time.sleep(2)
#     print('welcome %s to home page' %name)
#
#
# index(x=1,y=2,z=3)
# home('egon')



# 思考题（选做），叠加多个装饰器，加载顺序与运行顺序
# @deco1 # index=deco1(deco2.wrapper的内存地址)
# @deco2 # deco2.wrapper的内存地址=deco2(deco3.wrapper的内存地址)
# @deco3 # deco3.wrapper的内存地址=deco3(index)
# def index():
#     pass



# 总结无参装饰器模板
# def outter(func):
#     def wrapper(*args,**kwargs):
#         # 1、调用原函数
#         # 2、为其增加新功能
#         res=func(*args,**kwargs)
#         return res
#     return wrapper








def auth(func):
    def wrapper(*args,**kwargs):
        # 1、调用原函数
        # 2、为其增加新功能
        name=input('your name>>: ').strip()
        pwd=input('your password>>: ').strip()
        if name == 'egon' and pwd == '123':
            res=func(*args,**kwargs)
            return res
        else:
            print('账号密码错误')
    return wrapper



@auth
def index():
    print('from index')

index()




















"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""


# 一、叠加多个装饰器的加载、运行分析（了解***）

def deco1(func1): # func1 = wrapper2的内存地址
    def wrapper1(*args,**kwargs):
        print('正在运行===>deco1.wrapper1')
        res1=func1(*args,**kwargs)
        return res1
    return wrapper1

def deco2(func2): # func2 = wrapper3的内存地址
    def wrapper2(*args,**kwargs):
        print('正在运行===>deco2.wrapper2')
        res2=func2(*args,**kwargs)
        return res2
    return wrapper2

def deco3(x):
    def outter3(func3): # func3=被装饰对象index函数的内存地址
        def wrapper3(*args,**kwargs):
            print('正在运行===>deco3.outter3.wrapper3')
            res3=func3(*args,**kwargs)
            return res3
        return wrapper3
    return outter3


# 加载顺序自下而上(了解)
@deco1      # index=deco1(wrapper2的内存地址)        ===> index=wrapper1的内存地址
@deco2      # index=deco2(wrapper3的内存地址)        ===> index=wrapper2的内存地址
@deco3(111) # ===>@outter3===> index=outter3(index) ===> index=wrapper3的内存地址
def index(x,y):
    print('from index %s:%s' %(x,y))

# 执行顺序自上而下的，即wraper1-》wrapper2-》wrapper3
index(1,2) # wrapper1(1,2)

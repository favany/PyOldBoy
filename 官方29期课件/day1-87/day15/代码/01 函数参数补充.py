"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""

# 1. 命名关键字参数（了解）
#  命名关键字参数：在定义函数时，*后定义的参数，如下所示，称之为命名关键字参数
# 特点：
# 1、命名关键字实参必须按照key=value的形式为其传值
# def func(x,y,*,a,b): # 其中，a和b称之为命名关键字参数
#     print(x,y)
#     print(a,b)
#
# # func(1,2,b=222,a=111)

# 示例
# def func(x,y,*,a=11111,b):
#     print(x,y)
#     print(a,b)
#
# func(1,2,b=22222)

# 2. 组合使用（了解）
# 形参混用的顺序：位置新参，默认形参,*args,命名关键字形参，**kwargs
# def func(x,y=111,*args,z,**kwargs):
#     print(x)
#     print(y)
#     print(args)
#     print(z)
#     print(kwargs)
#


# 实参混用的顺序：
def func(x,y,z,a,b,c):
    print(x)
    print(y)
    print(z)
    print(a)
    print(b)
    print(c)

# func(111,y=222,*[333,444],**{'b':555,'c':666})
# func(111,y=222,333,444,b=555,c=666)

# func(111,*[333,444],a=222,**{'b':555,'c':666})
# func(111,333,444,a=222,b=555,c=66)

# func(111,*[333,444],**{'b':555,'c':666},a=222,)
func(111,3333,4444,b=555,c=666,a=222)


# func(1)
# func(x=1)
# func(1,x=1)
# func(*'hello')
# func(**{})
# func(*'hell',**{})
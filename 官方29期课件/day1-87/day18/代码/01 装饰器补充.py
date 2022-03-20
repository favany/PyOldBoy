"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""

#偷梁换柱，即将原函数名指向的内存地址偷梁换柱成wrapper函数
#        所以应该将wrapper做的跟原函数一样才行
from functools import wraps

def outter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """这个是主页功能"""
        res = func(*args, **kwargs) # res=index(1,2)
        return res

    # 手动将原函数的属性赋值给wrapper函数
    # 1、函数wrapper.__name__ = 原函数.__name__
    # 2、函数wrapper.__doc__ = 原函数.__doc__
    # wrapper.__name__ = func.__name__
    # wrapper.__doc__ = func.__doc__

    return wrapper



@outter # index=outter(index)
def index(x,y):
    """这个是主页功能"""
    print(x,y)


print(index.__name__)
print(index.__doc__) #help(index)










index(1,2) # wrapper(1,2)




















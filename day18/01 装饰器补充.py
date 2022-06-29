# @File      : 01 装饰器补充
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/6/25 9:06 AM
# @Info      :

from functools import wraps


def outer(func):
    @wraps(func)  # 将原函数的属性赋值给 wrapper，可加可不加
    def wrapper(*args, **kwargs):
        """ 你好 """
        res = func(*args, **kwargs)
        return res
    """
    将 原函数的属性赋值给 wrapper
    @wraps(func)
    """
    # wrapper.__name__ = func.__name__
    # wrapper.__doc__ = func.__doc__
    return wrapper


@outer
def index(x, y):
    print(x, y)

# index.__name__ = 原函数.__name__
# index.__doc__ = 原函数.__doc__

# 偷梁换柱 将原函数名指向的内存地址偷梁换柱成wrapper

print(index.__name__)




"""
@Time    : 2022/6/29 13:54
@Author  : 刘俊 jun.liu@deepfinance.com
@File    : 03 三元表达式.py
"""

x = 1
y = 2

"""
if x > y:
    return x
else:
    return y
"""

"""
三元表达式
语法格式：条件成立时的返回值 if 判断条件 else 条件不成立时的返回值
"""

res = x if x > y else y


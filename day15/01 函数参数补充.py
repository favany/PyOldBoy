# 1. 命名关键字参数（了解） keyword-only arguments

# 在定义函数时，*后定义的参数，如下所示，称之为命名关键字参数

"""
特点：
1.命名关键字实参必须按照key = value 的形式传值.

"""

def func(x, y, *, a, b): # 其中，a 和 b 称之为命名关键字函数
    print(x, y)
    print(a, b)

# func(1, 2)  # TypeError: func() missing 2 required keyword-only arguments: 'a' and 'b'
func(1, 2, a = 3, b = 4)

"""
>>
1 2
3 4
"""


def func(x, y, *, a=123, b):  # 其中，a 和 b 称之为命名关键字函数
    print(x, y)
    print(a, b)
func(1, 2, b=2)

"""
>>
1 2
123 2
"""


# 2. 组合使用（了解）
# 位置形参，默认形参，*args，命名关键字形参， **kwargs

def func(x, y=111, *args, z, **kwargs):
    print(x, y)
    print(args)
    print(z)
    print(kwargs)

# 实参混用的顺序
def func(x, y, z, a, b, c):
    print(x, y, z, a, b, c)

# 1 2 3 是位置形参，a b c是关键字实参
func(1, *[2, 3], a = 4, **{'b': 5, "c": 6})  # 1 2 3 4 5 6
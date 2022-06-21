# @File      : 03 匿名函数
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/6/19 6:01 PM
# @Info      :

"""
1. 有名函数
func = 函数的内存地址
"""
def func(x, y):
    return x+y


"""
2. 匿名函数
"""
lambda x,y: x + y


"""
3. 调用匿名函数
方式一：
"""
re = (lambda x, y: x + y)(1,2)
print(re)

"""
方式二：
"""
func = lambda x, y : x + y
re = func(1, 2)
print(re)

"""
4. 匿名用于临时调用一次的场景：更多的是将匿名函数与其他函数配合使用.
"""



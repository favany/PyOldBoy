"""
@Time    : 2022/6/30 15:43
@Author  : 刘俊 jun.liu@deepfinance.com
@File    : 05 函数的递归调用.py
"""

"""
函数的递归调用：
    函数嵌套调用的一种特殊形式
    
具体是指：
    在调用一个函数的过程中，又直接或间接地调用到本身

"""

# 一段代码的循环运行方案有两种：
# 方案一：while、for 循环
# while True:
#     print(111)

# 方案二：递归的本质是循环
# 直接调用本身
'''
def f1():
    print('是我是我还是我')
    f1()

f1()
'''

# 间接调用本身
'''
def f1():
    print('===> f1')
    f2()

def f2():
    print('===> f1')
    f1()
    
f2()
'''

"""
二、需要强调的一点
Python 没有尾递归优化
递归不应该无限地调用下去，必须在满足某种条件下结束递归
"""


# def func(n):
#     if n > 10:
#         return
#     print(n)
#     func(n + 1)
#
#
# func(0)

"""
三、递归的两个阶段：

回溯 一层一层调用下去

age(5) = age(4) + 10
age(4) = age(3) + 10
age(3) = age(2) + 10
age(2) = age(1) + 10
age(1) = 18

递推 满足某种结束条件，结束递归调用，然后一层一层返回

age(2) = age(1) + 18 = ...
age(3) = age(2) + 18 = ...
....
"""

# 四、递归的应用
l = [1, 2, [3, 4, [5]]]

def f1(l):
    for x in l:
        if type(x) is list:
            # 如果是列表，应该再循环，再判断
            f1(x)
        else:
            print(x)

f1(l)

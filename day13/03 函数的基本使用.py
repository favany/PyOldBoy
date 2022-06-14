# @File      : 03 函数的基本使用
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/6/14 8:14 AM
# @Info      :

'''
1. 什么是函数
    函数相当于具备某一功能的工具。
    函数的使用必须遵循先定义、后调用的规则

2. 为何要用函数
    - 代码荣誉，程序的组织结构不清晰，可读性差
    - 代码冗余
    - 可维护性、扩展性差

3. 如何用函数
- 先定义

def 函数名(参数1, 参数2, ...):   * 参数可有可无
    """描述"""                  * 描述可有可无
    函数体
    return 值                  * 返回值可有可无
- 后调用
- 返回值
'''


# 形式一：无参函数
def func():
    print('a')


func()

'''
定义函数发生的事情
1. 申请内存空间，保存函数体代码
2. 将上述内存地址绑定函数名
3. 定义函数不会执行函数体代码，但是会检测函数体语法

调用函数发生的事情
1. 通过函数名，找到内存地址
2. 加括号是在触发函数体代码

'''

# 示范1
# x = 1
# def bar():
#     print('from bar')
#
#
# def foo():
#     print(x)
#     print('foo runs', foo)
#
# foo()

# 示范2
def foo():
    bar()
    print('foo runs', foo)

foo()

def bar():
    print('from bar')


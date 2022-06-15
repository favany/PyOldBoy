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


'''
定义函数发生的事情
1. 申请内存空间，保存函数体代码
2. 将上述内存地址绑定函数名
3. 定义函数不会执行函数体代码，但是会检测函数体语法

调用函数发生的事情
1. 通过函数名，找到内存地址
2. 加括号是在触发函数体代码

'''


# 形式一：无参函数
def func():
    print('a')


func()



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
# def foo():
#     bar()
#     print('foo runs', foo)
#
# def bar():
#     print('from bar')
#
# foo()


# 示范3
# def foo():
#     bar()
#     print('foo runs', foo)
#
#
# foo()  # NameError: name 'bar' is not defined
#
#
# def bar():
#     print('from bar')


# 形式二 有参函数


def func(x, y):  # 参数相当于原材料
    return x + y   # 返回值相当于产品


func(1, 2)


# 形式三 空函数，函数体代码为pass (...)

def func(x, y):
    ...


# 二、调用函数

# 1. 语句形式：只加括号调用函数
func(1, 2)

# 2. 表达式形式：
res = func(1, 2)  # 赋值表达式

# func(1, 2) * 10  # 数学表达式


# 3. 作为参数调用

func(func(1, 2), 3) # 把函数的返回值作为参数


# 三、函数返回值

# return 是函数结束的标志。一旦运行到 return ，会立即终止运行。并将return 后的值作为函数体的结果返回。

# 1. 返回None：函数体内没有return 或者 return None

# 2. 返回一个值
# return value

# 3. 返回多个值

def func():
    return 1, 2, [1,2]


re = func()
print(re, type(re))  # (1, 2, [1, 2]) <class 'tuple'>




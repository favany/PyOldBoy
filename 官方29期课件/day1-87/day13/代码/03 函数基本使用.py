"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128

1、什么是函数
    函数就相当于具备某一功能的工具
    函数的使用必须遵循一个原则：
        先定义
        后调用
2、为何要用函数
    1、组织结构不清晰，可读性差
    2、代码冗余
    3、可维护性、扩展性差

3、如何用函数
        先定义
            三种定义方式
        后调用
            三种调用方式

        返回值
            三种返回值的形式

"""
# 一、先定义
# 定义的语法
'''
def 函数名(参数1,参数2,...):
    """文档描述"""
    函数体
    return 值
'''


# 形式一：无参函数
# def func():
#     # x
#     # print(
#     print('哈哈哈')
#     print('哈哈哈')
#     print('哈哈哈')

# 定义函数发生的事情
# 1、申请内存空间保存函数体代码
# 2、将上述内存地址绑定函数名
# 3、定义函数不会执行函数体代码，但是会检测函数体语法

# 调用函数发生的事情
# 1、通过函数名找到函数的内存地址
# 2、然后加口号就是在触发函数体代码的执行
# print(func)
# func()

# 示范1
# def bar(): # bar=函数的内存地址
#     print('from bar')
#
# def foo():
#     # print(bar)
#     bar()
#     print('from foo')
#
# foo()

# 示范2
# def foo():
#     # print(bar)
#     bar()
#     print('from foo')
#
# def bar():  # bar=函数的内存地址
#     print('from bar')
#
# foo()

# 示范3
# def foo():
#     # print(bar)
#     bar()
#     print('from foo')
#
# foo()
#
# def bar():  # bar=函数的内存地址
#     print('from bar')

# 形式二：有参函数
# def func(x,y): # x=1  y=2
#     print(x,y)
# func(1,2)

# 形式三：空函数,函数体代码为pass
def func(x, y):
    pass


# 三种定义方式各用在何处
# 1、无参函数的应用场景
# def interactive():
#     name=input('username>>: ')
#     age=input('age>>: ')
#     gender=input('gender>>: ')
#     msg='名字：{} 年龄：{} 性别'.format(name,age,gender)
#     print(msg)
#
# interactive()
# interactive()
# interactive()
# interactive()

# 2、有参函数的应用场景
# def add(x,y): # 参数-》原材料
#     # x=20
#     # y=30
#     res=x + y
#     # print(res)
#     return res # 返回值-》产品
#
# # add(10,2)
# res=add(20,30)
# print(res)

# 3、空函数的应用场景
# def auth_user():
#     """user authentication function"""
#     pass
#
# def download_file():
#     """download file function"""
#     pass
#
# def upload_file():
#     """upload file function"""
#     pass
#
# def ls():
#     """list contents function"""
#     pass
#
# def cd():
#     """change directory"""
#     pass


# 二、调用函数
# 1、语句的形式:只加括号调用函数
# interactive()
# add(1,2)

# 2、表达式形式：
# def add(x,y): # 参数-》原材料
#     res=x + y
#     return res # 返回值-》产品
# 赋值表达式
# res=add(1,2)
# print(res)
# 数学表达式
# res=add(1,2)*10
# print(res)

# 3、函数调用可以当做参数
# res=add(add(1,2),10)
# print(res)

# 三、函数返回值
# return是函数结束的标志，即函数体代码一旦运行到return会立刻
# 终止函数的运行，并且会将return后的值当做本次运行的结果返回：
# 1、返回None：函数体内没有return
#             return
#             return None
#
# 2、返回一个值：return 值
# def func():
#     return 10
#
# res=func()
# print(res)

# 3、返回多个值：用逗号分隔开多个值，会被return返回成元组
def func():
    return 10, 'aa', [1, 2]

res = func()
print(res, type(res))




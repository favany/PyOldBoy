
# 精髓 可以把函数当成变量去用

# func = 内存地址

def func():
    print("from func")

# 1. 可以赋值
f = func
print(f, func)
# f()

# 2. 可以把函数（的内存地址）当作参数传递给另一个函数
def foo(x): # x = func 的内存地址
    # print(x)
    x()

foo(func)  # foo(func内存地址)

# 3. 可以把函数当作另一个函数的返回值
def foo(x):  # x = func 的内存地址
    return x  # return func 的内存地址

res = foo(func) # foo （func的内存地址）
print(res)  # res = func的内存地址

res()

# 4. 可以当作容器类型的一个元素
<<<<<<< Updated upstream
l = [func, ]
print(l)  # [<function func at 0x103723f70>]
l[0]()  # from func


dic = {'k1': func}
dic['k1']()  # from func
=======
# l = [func, ]
# print(l)
# l[0]()


dict = {'k1': func}
print(dict)
dict['k1']()
>>>>>>> Stashed changes


def login():
    print("登陆功能")

<<<<<<< Updated upstream
def transfer():
    print("转账功能")

def check_balance():
    print("查询余额")

def withdraw():
    print("提现")

def register():
    print("注册")

func_dict = {"0": ["退出", None], "1": ["登陆", login], "2": ["转账", transfer], "3": ["查询余额", check_balance], "4": ["提现", withdraw], "5": ["注册", register]}

while True:
    for k in func_dict:
        print(k, func_dict[k][0])
    choice = input("请输入命令编号：").strip()
    if not choice.isdigit():
        print("必须输入编号")
        continue

    if choice == '0':
        break

    if choice in func_dict:
        func_dict[choice][1]()
    else:
        print("输入的指令不存在")

    # if choice == "1":
    #     login()
    # elif choice == "2":
    #     transfer()
    # elif choice == "3":
    #     check_balance()
    # else:
    #     print("输入的指令不存在")

# 函数的嵌套调用
# 1. 函数的嵌套调用：在调用一个函数的过程中，又调用其他函数
def max2(x, y):
    if x > y:
        return x
    else:
        return y


def max4(a, b, c, d):
    # 第一步：比较a, b 得到 res1
    res1 = max2(a, b)
    # 第二步：比较res1, c 得到 res2
    res2 = max2(res1, c)
    # 第三步：比较res2, d 得到 res3
    res3 = max2(res2, d)

    return res3

res = max4(1, 2, 3, 4)
print(res)

# 函数的嵌套定义： 在函数内定义其他函数
# 函数内定义的函数在外部调用不到

def f1():
    def f2():
        ...

"""
闭包函数 = 名称空间与作用域 + 函数嵌套 + 函数对象
核心点：名字的查找关系是以函数定义阶段为准的.

什么是闭包函数
闭函数 指的是该函数是定义在一个函数内的（内嵌函数）
包函数 值的是该函数包含对外层函数作用域名字的引用（不是全局作用域）
"""

def f1():
    x = 1
    def f2(): # 闭包函数
        print(x)
    return f2

x = 1111
f = f1()  # f 就是 f2
print(f)  # <function f1.<locals>.f2 at 0x1034909d0>

"""
三、为何要有闭包函数、闭包函数的应用
两种为函数传参的方式
方式一、直接把函数体需要的参数定义成形参
def f2(x):
    print(x)
方式二：
def f1():
    x = 3
    def f2():
        print(x)
    return f2
"""
=======

def transfer():
    print("转账")


def check_balance():
    print("查询余额")
>>>>>>> Stashed changes

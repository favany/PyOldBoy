

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
def foo(x):
    return x

res = foo(func)
print(res)

# 4. 可以当作容器类型的一个元素
l =
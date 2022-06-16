x = 111

# 在局部需要修改全局的名字对应的值（不可变类型），需要用 global
def func():
    global x  # 声明x 是全局的名字，无需再造新的名字
    x = 222

func()
print(x)  # 222

# 而全局的可变类型，可以直接修改

l = [1, 2]
def func():
    l.append(3)

func()
print(l)  # [1, 2, 3]

# nonlocal （了解）
x = 0
def f1():
    x = 1
    def f2():
        nonlocal x  # 指定上一层的 x
        x = 2 # 想要修改 x= 1 处的 x 值
    f2()
    print("f1 内的 x:", x)  # f1 内的 x: 2
f1()

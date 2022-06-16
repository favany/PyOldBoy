"""
名称空间

栈区：存放名字和内存地址绑定关系

把栈区划块：
- 全局范围
    - 内置名称空间
    - 全局名称空间

- 局部范围
    - 局部名称空间

堆区：存放内存地址和值

一、名称空间 namespaces 存放名字的地方 是对栈区的划分

有了名称空间之后，就可以在栈区中存放相同的名字。名称空间分为三种。

1.1 内置名称空间
存放的名字：Python 解释器内置的名字
生命周期：Python解释器启动，则产生；Python解释器关闭，则销毁。

>>> print
<built-in function print>
>>> input
<built-in function input>


1.2 全局名称空间
存放的名字：运行顶级代码（不是函数内，也不是内置的），剩下的都是全局名称空间的名字.
生命周期：Python文件执行则产生，运行完毕后销毁。

import os

x = 3

if 2 > 1:
    y = 1

1.3 局部名称空间

存放的名字：在调用函数时，运行的函数体代码过程中，产生的名字

def func():
    a = 111
    b = 222

1.4 名称空间的加载顺序
内置名称空间 > 全局名称空间 > 局部名称空间


1.5 名称空间的加载顺序
局部名称空间 > 全局名称空间 > 内置名称空间

1.6 名字的查找优先级：当前所在的位置向上一层一层查找
- 内置名称空间
- 全局名称空间
- 局部名称空间

如果当前在局部名称空间：
 局部名称空间 -> 全局名称空间 -> 内置名称空间

input=333

如果当前在全局名称空间
全局名称空间 → 内置名称空间


"""

# 一

input = 222
def func():
    input = 444
    print(input)  # 444
func()

# 二

input = 222
def func():
    # input = 444
    print(input)  # 222
func()

# 三

# input = 222
def func():
    # input = 444
    print(input)  # <built-in function input>
func()


# 示范
def func():
    print(x)
x = 111
func()  # 111

# 示范二 名称空间的"嵌套"关系是以函数定义的阶段为准的，与调用位置无关

x = 1
def func():
    print(x)  # 1

def foo():
    x = 222
    func()

foo()

# 示范三 函数嵌套

input = 1
def f1():
    input = 2
    def f2():
        input = 3
        print(input)  # 3 -> 2 -> 1 -> 内置函数
    f2()

f1()

# 示范四
x = 1
def func():
    # print(x)  # UnboundLocalError: local variable 'x' referenced before assignment
    x = 2

func()


"""
二、作用域 => 作用范围

全局作用域：内置名称空间、全局名称空间。全局存活，全局有效（被所有函数共享）。

局部作用域：局部名称空间的名字，临时存活、局部有效。


"""

# LEGB

# built-in

# global
def f1():
    # enclosing
    def f2():
        # enclosing
        def f3():
            # local
            pass

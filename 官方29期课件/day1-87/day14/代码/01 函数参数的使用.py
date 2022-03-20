"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""


# 一 形参与实参介绍
# 形参：在定义函数阶段定义的参数称之为形式参数，简称形参,相当于变量名
def func(x, y):  # x=1，y=2
    print(x, y)


# 实参：在调用函数阶段传入的值称之为实际参数，简称实参，相当于变量值
# func(1,2)

# 形参与实参的关系：
# 1、在调用阶段，实参（变量值）会绑定给形参（变量名）
# 2、这种绑定关系只能在函数体内使用
# 3、实参与形参的绑定关系在函数调用时生效，函数调用结束后解除绑定关系

# 实参是传入的值，但值可以是以下形式
# 形式一：
# func(1,2)

# 形式二：
# a=1
# b=2
# func(a,b)

# 形式三：
# func(int('1'),2)
# func(func1(1,2,),func2(2,3),333)


# 二 形参与实参的具体使用
# 2.1 位置参数：按照从左到右的顺序依次定义的参数称之为位置参数
# 位置形参:在函数定义阶段，按照从左到右的顺序直接定义的"变量名"
#        特点：必须被传值，多一个不行少一个也不行
# def func(x,y):
#     print(x,y)
# func(1,2,3)
# func(1,)

# 位置实参:在函数调用阶段， 按照从左到有的顺序依次传入的值
#        特点：按照顺序与形参一一对应

# func(1,2)
# func(2,1)

# 2.2 关键字参数
# 关键字实参：在函数调用阶段，按照key=value的形式传入的值
#       特点：指名道姓给某个形参传值，可以完全不参照顺序
# def func(x,y):
#     print(x,y)

# func(y=2,x=1)
# func(1,2)

# 混合使用，强调
# 1、位置实参必须放在关键字实参前
# func(1,y=2)
# func(y=2,1)

# 2、不能能为同一个形参重复传值
# func(1,y=2,x=3)
# func(1,2,x=3,y=4)


# 2.3 默认参数
# 默认形参：在定义函数阶段，就已经被赋值的形参，称之为默认参数
#       特点：在定义阶段就已经被赋值，意味着在调用阶段可以不用为其赋值
# def func(x,y=3):
#     print(x,y)
#
# # func(x=1)
# func(x=1,y=44444)


# def register(name,age,gender='男'):
#     print(name,age,gender)
#
# register('三炮',18)
# register('二炮',19)
# register('大炮',19)
# register('没炮',19,'女')


# 位置形参与默认形参混用，强调：
# 1、位置形参必须在默认形参的左边
# def func(y=2,x):
#     pass

# 2、默认参数的值是在函数定义阶段被赋值的，准确地说被赋予的是值的内存地址
# 示范1：
# m=2
# def func(x,y=m): # y=>2的内存地址
#     print(x,y
# m=3333333333333333333
# func(1)

# 示范2：
# m = [111111, ]
#
# def func(x, y=m): # y=>[111111, ]的内存地址
#     print(x, y)
#
# m.append(3333333)
# func(1)

# 3、虽然默认值可以被指定为任意数据类型，但是不推荐使用可变类型
# 函数最理想的状态：函数的调用只跟函数本身有关系，不外界代码的影响
# m = [111111, ]
#
# def func(x, y=m):
#     print(x, y)
#
# m.append(3333333)
# m.append(444444)
# m.append(5555)
#
#
# func(1)
# func(2)
# func(3)


# def func(x,y,z,l=None):
#     if l is None:
#         l=[]
#     l.append(x)
#     l.append(y)
#     l.append(z)
#     print(l)

# func(1,2,3)
# func(4,5,6)

# new_l=[111,222]
# func(1,2,3,new_l)


# 2.4 可变长度的参数（*与**的用法）
# 可变长度指的是在调用函数时，传入的值（实参）的个数不固定
# 而实参是用来为形参赋值的，所以对应着，针对溢出的实参必须有对应的形参来接收

# 2.4.1 可变长度的位置参数
# I：*形参名：用来接收溢出的位置实参，溢出的位置实参会被*保存成元组的格式然后赋值紧跟其后的形参名
#           *后跟的可以是任意名字，但是约定俗成应该是args

# def func(x,y,*z): # z =（3,4,5,6）
#     print(x,y,z)

# func(1,2,3,4,5,6)

# def my_sum(*args):
#     res=0
#     for item in args:
#         res+=item
#     return res
#
# res=my_sum(1,2,3,4,)
# print(res)

# II: *可以用在实参中，实参中带*，先*后的值打散成位置实参
# def func(x,y,z):
#     print(x,y,z)
#
# # func(*[11,22,33]) # func(11，22，33)
# # func(*[11,22]) # func(11，22)
#
# l=[11,22,33]
# func(*l)

# III: 形参与实参中都带*
# def func(x,y,*args): # args=(3,4,5,6)
#     print(x,y,args)

# func(1,2,[3,4,5,6])
# func(1,2,*[3,4,5,6]) # func(1,2,3,4,5,6)
# func(*'hello') # func('h','e','l','l','o')


# 2.4.2 可变长度的关键字参数
# I：**形参名：用来接收溢出的关键字实参，**会将溢出的关键字实参保存成字典格式，然后赋值给紧跟其后的形参名
#           **后跟的可以是任意名字，但是约定俗成应该是kwargs
# def func(x,y,**kwargs):
#     print(x,y,kwargs)
#
# func(1,y=2,a=1,b=2,c=3)

# II: **可以用在实参中(**后跟的只能是字典)，实参中带**，先**后的值打散成关键字实参
# def func(x,y,z):
#     print(x,y,z)

# func(*{'x':1,'y':2,'z':3}) # func('x','y','z')
# func(**{'x':1,'y':2,'z':3}) # func(x=1,y=2,z=3)

# 错误
# func(**{'x':1,'y':2,}) # func(x=1,y=2)
# func(**{'x':1,'a':2,'z':3}) # func(x=1,a=2,z=3)


# III: 形参与实参中都带**
# def func(x,y,**kwargs):
#     print(x,y,kwargs)

# func(y=222,x=111,a=333,b=444)
# func(**{'y':222,'x':111,'a':333,'b':4444})




# 混用*与**：*args必须在**kwargs之前
# def func(x,*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# func(1,2,3,4,5,6,7,8,x=1,y=2,z=3)


def index(x,y,z):
    print('index=>>> ',x,y,z)

def wrapper(*args,**kwargs): #args=(1,) kwargs={'z':3,'y':2}
    index(*args,**kwargs)
    # index(*(1,),**{'z':3,'y':2})
    # index(1,z=3,y=2)

wrapper(1,z=3,y=2) # 为wrapper传递的参数是给index用的
# 原格式---》汇总-----》打回原形



# 2.5 命名关键字参数（了解）
# 2.6 组合使用（了解）















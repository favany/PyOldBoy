"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""
# 一：大前提：
# 闭包函数=名称空间与作用域+函数嵌套+函数对象
#        核心点：名字的查找关系是以函数定义阶段为准

# 二：什么是闭包函数
# "闭"函数指的该函数是内嵌函数
# "包"函数指的该函数包含对外层函数作用域名字的引用（不是对全局作用域）

# 闭包函数：名称空间与作用域的应用+函数嵌套
# def f1():
#     x = 33333333333333333333
#     def f2():
#         print(x)
#     f2()
#
#
# x=11111
# def bar():
#     x=444444
#     f1()
#
# def foo():
#     x=2222
#     bar()
#
# foo()



# 闭包函数：函数对象
# def f1():
#     x = 33333333333333333333
#     def f2():
#         print('函数f2：',x)
#     return f2
#
# f=f1()
# # print(f)
#
# # x=4444
# # f()
# def foo():
#     x=5555
#     f()
#
# foo()


# 三：为何要有闭包函数=》闭包函数的应用
# 两种为函数体传参的方式
# 方式一：直接把函数体需要的参数定义成形参
# def f2(x):
#     print(x)
#
# f2(1)
# f2(2)
# f2(3)

# 方式二：
# def f1(x): # x=3
#     x=3
#     def f2():
#         print(x)
#     return f2
#
# x=f1(3)
# print(x)
#
# x()



import requests

# 传参的方案一：
# def get(url):
#     response=requests.get(url)
#     print(len(response.text))
#
# get('https://www.baidu.com')
# get('https://www.cnblogs.com/linhaifeng')
# get('https://zhuanlan.zhihu.com/p/109056932')


# 传参的方案二：
def outter(url):
    # url='https://www.baidu.com'
    def get():
        response=requests.get(url)
        print(len(response.text))
    return get

baidu=outter('https://www.baidu.com')
baidu()

cnblogs=outter('https://www.cnblogs.com/linhaifeng')
cnblogs()

zhihu=outter('https://zhuanlan.zhihu.com/p/109056932')
zhihu()


















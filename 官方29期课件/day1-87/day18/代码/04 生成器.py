"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""
# 如何得到自定义的迭代器：
# 在函数内一旦存在yield关键字，调用函数并不会执行函数体代码
# 会返回一个生成器对象，生成器即自定义的迭代器
def func():
    print('第一次')
    yield 1
    print('第二次')
    yield 2
    print('第三次')
    yield 3
    print('第四次')


# g=func()
# print(g)
# 生成器就是迭代器
# g.__iter__()
# g.__next__()


# 会触发函数体代码的运行，然后遇到yield停下来，将yield后的值
# 当做本次调用的结果返回
# res1=g.__next__()
# print(res1)
#
#
# res2=g.__next__()
# print(res2)
#
# res3=g.__next__()
# print(res3)
#
# res4=g.__next__()



# len('aaa') # 'aaa'.__len__()

# next(g)    # g.__next__()
# iter(可迭代对象)     # 可迭代对象.__iter__()


# 应用案列
def my_range(start,stop,step=1):
    # print('start...')
    while start < stop:
        yield start
        start+=step
    # print('end....')


# g=my_range(1,5,2) # 1 3
# print(next(g))
# print(next(g))
# print(next(g))

for n in my_range(1,7,2):
    print(n)


# 总结yield：
# 有了yield关键字，我们就有了一种自定义迭代器的实现方式。yield可以用于返回值，但不同于return，函数一旦遇到return就结束了，而yield可以保存函数的运行状态挂起函数，用来返回多次值


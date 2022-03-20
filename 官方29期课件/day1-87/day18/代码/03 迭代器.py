"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""

'''
1、什么是迭代器
    迭代器指的是迭代取值的工具，迭代是一个重复的过程，每次重复
    都是基于上一次的结果而继续的，单纯的重复并不是迭代
    
2、为何要有迭代器
    迭代器是用来迭代取值的工具，而涉及到把多个值循环取出来的类型
    有：列表、字符串、元组、字典、集合、打开文件
    
    l=['egon','liu','alex']
    i=0
    while i < len(l):
        print(l[i])
        i+=1
        
    上述迭代取值的方式只适用于有索引的数据类型：列表、字符串、元组
    为了解决基于索引迭代器取值的局限性
    python必须提供一种能够不依赖于索引的取值方式，这就是迭代器


3、如何用迭代器
    
'''
# 1、可迭代的对象：但凡内置有__iter__方法的都称之为可迭代的对象
# s1=''
# # s1.__iter__()
#
# l=[]
# # l.__iter__()
#
# t=(1,)
# # t.__iter__()
#
# d={'a':1}
# # d.__iter__()
#
# set1={1,2,3}
# # set1.__iter__()
#
# with open('a.txt',mode='w') as f:
#     # f.__iter__()
#     pass

# 2、调用可迭代对象下的__iter__方法会将其转换成迭代器对象
d={'a':1,'b':2,'c':3}
d_iterator=d.__iter__()
# print(d_iterator)

# print(d_iterator.__next__())
# print(d_iterator.__next__())
# print(d_iterator.__next__())
# print(d_iterator.__next__()) # 抛出异常StopIteration


# while True:
#     try:
#         print(d_iterator.__next__())
#     except StopIteration:
#         break
#
# print('====>>>>>>') # 在一个迭代器取值取干净的情况下，再对其取值娶不到
# d_iterator=d.__iter__()
# while True:
#     try:
#         print(d_iterator.__next__())
#     except StopIteration:
#         break


# l=[1,2,3,4,5]
# l_iterator=l.__iter__()
#
# while True:
#     try:
#         print(l_iterator.__next__())
#     except StopIteration:
#         break


# 3、可迭代对象与迭代器对象详解
# 3.1 可迭代对象（"可以转换成迭代器的对象"）：内置有__iter__方法对象
#        可迭代对象.__iter__(): 得到迭代器对象

# 3.2 迭代器对象：内置有__next__方法并且内置有__iter__方法的对象
#        迭代器对象.__next__（）：得到迭代器的下一个值
#        迭代器对象.__iter__（）：得到迭代器的本身，说白了调了跟没调一个样子
# dic={'a':1,'b':2,'c':3}
#
# dic_iterator=dic.__iter__()
# print(dic_iterator is dic_iterator.__iter__().__iter__().__iter__())
#

# 4、可迭代对象：字符串、列表、元组、字典、集合、文件对象
# 迭代器对象：文件对象
# s1=''
# s1.__iter__()
#
# l=[]
# l.__iter__()
#
# t=(1,)
# t.__iter__()
#
#
# d={'a':1}
# d.__iter__()
#
# set1={1,2,3}
# set1.__iter__()
#
#
# with open('a.txt',mode='w') as f:
#     f.__iter__()
#     f.__next__()





# 5、for循环的工作原理：for循环可以称之为叫迭代器循环
d={'a':1,'b':2,'c':3}

# 1、d.__iter__()得到一个迭代器对象
# 2、迭代器对象.__next__()拿到一个返回值，然后将该返回值赋值给k
# 3、循环往复步骤2，直到抛出StopIteration异常for循环会捕捉异常然后结束循环
# for k in d:
#     print(k)


# with open('a.txt',mode='rt',encoding='utf-8') as f:
#     for line in f: # f.__iter__()
#         print(line)


# list('hello') #原理同for循环

# 6、迭代器优缺点总结
# 6.1 缺点：
# I、为序列和非序列类型提供了一种统一的迭代取值方式。
# II、惰性计算：迭代器对象表示的是一个数据流，可以只在需要时才去调用next来计算出一个值，就迭代器本身来说，同一时刻在内存中只有一个值，因而可以存放无限大的数据流，而对于其他容器类型，如列表，需要把所有的元素都存放于内存中，受内存大小的限制，可以存放的值的个数是有限的。

# 6.2 缺点：
# I、除非取尽，否则无法获取迭代器的长度
#
# II、只能取下一个值，不能回到开始，更像是‘一次性的’，迭代器产生后的唯一目标就是重复执行next方法直到值取尽，否则就会停留在某个位置，等待下一次调用next；若是要再次迭代同个对象，你只能重新调用iter方法去创建一个新的迭代器对象，如果有两个或者多个循环使用同一个迭代器，必然只会有一个循环能取到值。








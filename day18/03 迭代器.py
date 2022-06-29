# @File      : 03 迭代器
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/6/25 6:31 PM
# @Info      :

"""
1. 什么是迭代器
    迭代器是迭代取值的工具，迭代是一个重复的过程，每次重复都是基于上一次的结果而继续的，单纯的重复并不是迭代。
"""

count = 0
while count < 5:
    print(count)
    count += 1

l = ['jun', 'mophia', 'liu']
i = 0
while i < len(l):
    print(l[i])
    i += 1

"""
2. 为何要有迭代器
    迭代器是用来迭代取值的工具，而涉及到把多个值循环取出来的类型有：
    列表、字符串、元组、字典、集合、文件

    上述迭代取值的方式只适用于有索引的数据类型：列表、字符串、数组

    为了解决基于索引迭代器取值局限性， python 必须提供一种能不依赖于索引的取值方式，这就是迭代器

3. 如何用迭代器

    可迭代对象：内置有 __iter__ 方法的（即可以用这个方法转换为迭代器）都称之为可迭代的对象
    可迭代对象.__iter__() = 迭代器对象
    迭代器对象：内置有 __next__ 方法 并且内置有 __iter__ 方法的对象
    迭代器对象.next() = 得到迭代器的下一个值
    迭代器对象.__iter__() = 迭代器本身，调了和没调没区别

"""
s1 = ''
# s1.__iter__()

l = []
# l.__iter__()

t = (1,)
# t.__iter__()

d = {'a': 1, 'b': 2, 'c': 3}
d_iterator = d.__iter__()
print(d_iterator.__next__())  # <dict_keyiterator object at 0x103b34e50>
print(d_iterator.__next__())
print(d_iterator.__next__())

# print(d_iterator.__next__())  # 抛出异常 StopIteration
# print(d_iterator.__next__())

print(d_iterator is d_iterator.__iter__() is d_iterator.__iter__().__iter__())  # True


set1 = {1, 2, 3}
# set1.__iter__()

with open('a.txt', mode='w') as f:
    # f.__iter__()
    ...

"""
4. 可迭代对象

调用可迭代对象下的 __iter__ 方法会将其转换成迭代器对象
可迭代对象 是 可以转换成迭代器的对象
对同一个迭代器取值只能取一轮，取干净就不能再取了。


for 循环可以称之为迭代器循环

for 循环的工作原理
1. d.__iter__() 得到一个迭代器对象
2. 迭代器对象.__next__() 拿到一个返回值，然后将该值赋值给 k
3. 循环往复步骤 2 ，直到抛出 StopIteration 异常，for 循环会捕捉异常，然后结束循环

可迭代对象：字符串、列表、元组、字典、集合、文件对象
迭代器对象：文件对象
"""
for k in d:
    print(k)

while True:
    try:
        print(d_iterator.__next__())
    except StopIteration:
        break


with open('a.txt', mode='rt', encoding='utf-8') as f:
    for line in f:  # f.__iter__()
        print(line)

"""
迭代器优缺点总结

3.1优点：
1、为序列和非序列类型提供了一种统一的迭代取值方式。
2、惰性计算：迭代器对象表示的是一个数据流，可以只在需要时才去调用next来计算出一个值，
就迭代器本身来说，同一时刻在内存中只有一个值，因而可以存放无限大的数据流，而对于其他容
器类型，如列表，需要把所有的元素都存放于内存中，受内存大小的限制，可以存放的值的个数是
有限的。

3.2 缺点：
1、除非取尽，否则无法获取迭代器的长度

2、只能取下一个值，不能回到开始，更像是‘一次性的’，迭代器产生后的唯一目标就是重复执行next方法直到值取尽，否则就会停留在某个位置，
等待下一次调用next；若是要再次迭代同个对象，你只能重新调用iter方法去创建一个新的迭代器对象，
如果有两个或者多个循环使用同一个迭代器，必然只会有一个循环能取到值。


"""
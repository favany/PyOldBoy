"""
生成器

如何得到自定义的迭代器
在函数中存在 yield 关键字，会返回
会返回一个生成器，生成器就是自定义的迭代器
"""


def func():
    print('第一次')
    yield 1
    print('第二次')
    yield 2
    print('第三次')
    yield 3


g = func()  # <generator object func at 0x1071f6cf0>
print(g)

# 生成器就是迭代器

# 会触发函数体代码的运行，然后遇到 yield 停下来，将 yield 后面的值当作本次调用的结果
res1 = g.__next__()
print(res1)

res2 = g.__next__()
print(res2)

res3 = g.__next__()
print(res3)

# StopIteration
# res4 = g.__next__()
# print(res4)

"""
'aaa'.__len__() <=> len('aaa')
g.__next__() <=>  next(g)
l.__iter__() <=>  iter(g)
"""

# 应用案例
def my_range(start, stop, step):
    print("start...")
    while start < stop:
        yield start
        start += step
    print("end...")

# g = my_range(1, 5, 2)
# print(next(g))
# print(next(g))

for n in my_range(1, 7, 2):
    print(n)



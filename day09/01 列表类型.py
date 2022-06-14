# @File      : 01 列表类型
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Time      : 2022/6/7 11:06 AM
# @Info      : 列表

# 1. 作用：按照位置存放多个值，并且索引对应值。

# 2. 定义
l = [1, 1.2, 'a'] # l = list([1, 1.2, 'a'])

# 3. 类型转换
# 能被 for 循环的
# 字符串 转 列表
res = list('mophia')
print(res)  # ['m', 'o', 'p', 'h', 'i', 'a']

# 字典 转 列表
res = list({'k1': 111, 'k2': 222, 'k3': 333})  # 注：字典是无序的
print(res)  # ['k1', 'k2', 'k3']

# 4. 内置方法

# 优先掌握的操作：
# .1 按索引取值（正向存取 + 反向存取）：既可存，也可取
l = ['mophia', 666, 999]

# 正向取
print(l[0])  # mophia

# 反向取
print(l[-1])  # 999

# 也可以改
# 索引存在，则修改对应的值
l[2] = 555
print(l)  # ['mophia', 666, 555]

# 无论存还是取，索引不存在，则报错.
# l[3] = 666  # IndexError: list assignment index out of range

# .2 追加值
l.append(333)
print(l)  # ['mophia', 666, 555, 333]

# .3 插入值
l.insert(0, 'insert')
print(l)  # ['insert', 'mophia', 666, 555, 333]

# list1.extend(list2) 展开列表 list2 ，并追加到 list1

"""
代码实现
for item in new_l:
    l.append(item)
"""

l = [0]
l.extend([1, 2, 3])
print(l)  # [0, 1, 2, 3]
l.extend('abc')
print(l)  # [0, 1, 2, 3, 'a', 'b', 'c']


# 拓展：亚伦阿瑟36题

# .4 删除
# 方法一：通用的删除方法 del
# 只是单纯删除，没有返回值
l = [1, 2, 3]
del l[1]  # 不支持赋值语法
print(l)  # [1, 3]

# 方法二：l.pop(index) 根据索引删除
l = [1, 2, 3]
pop_item = l.pop()  # 不指定索引，默认删除最后一个. 会返回删除的那个值
print(l, pop_item)  # [1, 2] 3

l = [1, 2, 3]
pop_item = l.pop(1)
print(l, pop_item)  # [1, 3] 2

# 方法三: l.remove(val) 根据元素值删除
l = [1, [1, 2], 3]
l.remove([1, 2])  # 没有返回值
print(l)

# .5 切片
# 切片是拷贝行为，不改变原来的数组
# [开始:结束（顾头不顾尾）:步长]

l = [0, 1, 2, 3, 4]
print(l[0:3])  # [0, 1, 2]
print(l[0:5:2])  # [0, 2, 4]

# 切片等同于拷贝行为（浅拷贝）。原列表变了，新列表跟着变化。内存地址一致。
new_l = l[:] # l.copy()

# 反向列表
print(l[::-1])  # 反向列表

# .6 长度

print(len(l))  # 5

# .7 判断成员是否存在 in not in
print('mophia' in l)  # False

# .8 循环
for val in [1, 2, 3]:
    print(val)

# 需要掌握的操作
l = [1, 'a', 'b', 'a', 2, 3]

# list.count(val)  统计个数
print(l.count('a'))  # 2


# list.count(val) 返回首个索引，找不到则报错
print(l.index('a'))  # 1

# list.reverse() 列表反转
l.reverse()
print(l)  # [3, 2, 'a', 'b', 'a', 1]

# list.sort() 排序
# 默认升序；reverse=True 则设置为降序
print([1, 2, 3])  # [1, 2, 3]
# 字符串可以按照ASCII码比大小. 按照位数依次比大小 'z' > 'abc'
print('a' < 'b')  # True

# 列表也可以比大小，原理同字符串一样. 按照位数依次比大小. 对应位置的元素必须是同种类型.


# list.clear() 列表清空
l.clear()
print(l)  # []










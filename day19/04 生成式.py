"""
@Time    : 2022/6/29 14:04
@Author  : 刘俊 jun.liu@deepfinance.com
@File    : 04 生成式.py
"""

# 1. 列表生成式

l = ['alex_666', 'tom_666', 'jerry']

"""
new_l = []
for name in l:
    if name.endswith('_666'):
        new_l.append(name)
"""

new_l = [name for name in l if name.endswith('_666')]
print(new_l)  # ['alex_666', 'tom_666']

# 把小写字母全变成大写
new_l = [name.upper() for name in l]
print(new_l)  # ['ALEX_666', 'TOM_666', 'JERRY']

# 把所有的名字去掉后缀 _dsb
new_l = [name.replace('_666', '') for name in l]
print(new_l)  # ['alex', 'tom', 'jerry']


# 2. 字典生成式
keys = ['name', 'age']
dict = {key:None for key in keys}
print(dict)


items = [('name', 'egon'), ('age', 18), ('gender', 'male')]
res = {k: v for k, v in items if k != 'gender'}
print(res)

# 3. 集合生成式
keys = ['name', 'age', 'gender']
set1 = {key for key in keys}
print(set1, type(set1))  # {'name', 'gender', 'age'} <class 'set'>


# 4.生成器表达式**
g = (i for i in range(10) if i>3)
print(g, type(g)) # <generator object <genexpr> at 0x1067f6120> <class 'generator'>

# !!!! ⚠️ ！！！！
g = (i for i in range(10) if i > 3)
print(g)
print(next(g))

with open('notes.txt', mode='rt', encoding='utf8') as f:
    # 方式一
    res = 0
    for line in f:
        res += len(line)
    print(res)

    # 方式二
    res = sum([len(line) for line in f])
    print(res)

    # 方式三：效率最高
    # res = sum((len(line) for line in f))
    # 上述可以简写为如下形式：
    res = sum(len(line) for line in f)
    print(res)




# @File      : 04 字典类型
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/6/7 5:14 PM
# @Info      : 字典

# 1. 作用
# 用来记录多个值。多个值是用key来对应值。key通常是字符串类型，对value有描述性功能。

# 2. 定义
# 在 {} 内用逗号分隔开多个 key: value 其中 value 可以是任意类型 但是 key 必须是 不可变类型且不能重复。

d = {'k1': 1, (1, 2, 3): 2}  # d = dict(...)
print(d['k1'], d[(1, 2, 3)])  # 1 2
print(type(d))  # <class 'dict'>

# key 不能重复
d = {'k1': 1, 'k1': 2, 'k1':3}
print(d)  # {'k1': 3}

# 空字典
d = dict()  # 或 d = {}
print(d, type(d))  # {} <class 'dict'>

# key = value 的赋值方法
d = dict(x=1, y=2, z=3)
print(d, type(d))  # {'x': 1, 'y': 2, 'z': 3} <class 'dict'>

# 3. 类型转换
# 嵌套数组/元组创建字典

# dict()
# 1. 原理1
info = [
    ['name', 'mophia'],
    ('age', 23)
]
d = {}
for item in info:
    d[item[0]] = item[1]
print(d)  # {'name': 'mophia', 'age': 23}

# 2. 原理2
info = [
    ['name', 'mophia'],
    ('age', 23)
]
d = {}
for k, v in info:
    d[k] = v
print(d)  # {'name': 'mophia', 'age': 23}

# 3.
info = [
    ['name', 'mophia'],
    ('age', 23)
]
d = dict(info)
print(d)  # {'name': 'mophia', 'age': 23}


# 由 key 快速初始化字典
# 1.
keys = ['name', 'age']
value = None

d = {}
for k in keys:
    d[k] = None
print(d)  # {'name': None, 'age': None}

# 2.
d = {}.fromkeys(keys, None)
print(d)  # {'name': None, 'age': None}


# 4. 内置方法
# 优先掌握的操作：
# 1. 按 key 存取值：可存可取
d = {'k1': 1}

# 赋值操作：key存在，则修改值；key 不存在，则创建新值
d['k1'] = 2
d['k2'] = 3
print(d)  # {'k1': 2, 'k2': 3}

# 2. len() 统计元素个数

d = {'k1': 1, 'k1': 2, 'k1':3}
print(len(d))  # 1

# 3. 成员运算 in / not in : 根据 key
d = {'k1': 1, 'k2': 2}
print('k1' in d)  # True

# 4. 删除
# 4.1 通用删除
d = {'k1': 1, 'k2': 2}
del d['k1']
print(d)  # {'k2': 2}

# 4.2 pop 删除：根据 key 删除元素，返回删除 key 对应的 value 值
# d.pop(key)
d = {'k1': 1, 'k2': 2}
res = d.pop('k1')
print(d, res)  # {'k2': 2} 1

# 4.3 popitem 删除：随机删除，返回一个元组(删除的key, 删除的value)
d = {'k1': 1, 'k2': 2}
res = d.popitem()
print(d, res)  # {'k1': 1} ('k2', 2)

# 5. 键 keys() 值 values() 键值对 items()
d = {'k1': 1, 'k2': 2}
print(d.keys(), d.values(), d.items())  # dict_keys(['k1', 'k2']) dict_values([1, 2]) dict_items([('k1', 1), ('k2', 2)])
print(dict(d.keys()))  # {'k': '2'}

# 6. for 循环
for k in d.keys():
    print(k)

for k in d:  # 也是循环 keys 循环同上
    print(k)

for k, v in d.items():
    print(k, v)

# 获取 key value item 对应的列表
print(d.keys(), list(d.keys()))
print(d.values(), list(d.values()))
print(d.items(), list(d.items()))

# 需要掌握
# 其他内置方法
d = {'k1': 1, 'k2': 2}

# 用新字典更新原字典
# 修改已存在的key对应的值，新增不存在的key对应的值
d.update({'k2': 22, 'k3': 33})


# print(d['k10']) # key 不存在会报错

# dict.get() 🌟（常用）
# 根据 key 取值，容错性更好

print(d.get('k1'))  # 1
print(d.get('k10'))  # key 不存在不报错，返回 None

# dict.setdefault(key, value)
# 如果 key 有，则不添加；如果 key 没有，则 dict[key] = value. 返回当前字典中 key 对应的值.

d = {'k1': 1, 'k2': 2}
if 'k1' in d:
    ...  # 新语法，等同于pass
else:
    d['k1'] = 1

# 清空字典
d.clear()


# 列表和元组是有序的，字典是无序的；都能存多个值，称为容器类型；列表和字典是可变类型，元组是不可变类型。

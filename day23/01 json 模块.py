# @File      : 01 json与pickle模块
# @Author    : 刘俊 mophia
# @Time      : 2022/5/30 10:23 PM

# 什么是序列化/反序列化？
# 序列化是指把内存的数据类型转换成一个特定格式的内容，该格式的内容可用于存储或者传输给其他平台使用。
# 序列化：内存中的数据类型 -> 序列化 -> 特定的格式 json 或 pickle 格式
# 反序列化：特定的格式 json 或 pickle 格式 -> 序列化 -> 内存中的数据类型

# 序列化的例子：{"a": 111} -> 序列化 str({"a": 111}) -> '{"a": 111}'
#            '{"a": 111}' -> 反序列化 eval('{"a": 111}') -> {"a": 111}

# 为何要序列化？
# 序列化把进行数据转化，用于
# 1. 存储 -- 存档
# 2. 传输给其他平台使用 -- 跨平台数据交互

# 强调：
#   针对用途 1 的特定格式：专用格式 pickle 只有 python 可以识别
#   针对用途 2 的特定格式：json

# 如何序列化？

import json
jsonRe = json.dumps([1, 'aaa', True])
# print(jsonRe, type(jsonRe))
# [1, "aaa", true] <class 'str'>

# 把 json 写入文件的复杂方法
# with open('test.json', mode='wt', encoding='utf-8') as f:
#     f.write(jsonRe)

# 将 json 写入文件的简单方法
with open('test2.json', mode='wt', encoding='utf-8') as f:
    json.dump([1, 'aaa', True], f)

re = json.loads(jsonRe)

# print(re, type(re))
# [1, 'aaa', True] <class 'list'>

# 从文件读取 json 格式的字符串进行反序列化的简单方法
with open('test.json', mode='rt', encoding="utf-8") as f:
    l = json.load(f)
    print(l, type(l))  # [1, 'aaa', True] <class 'list'>

# 从文件读取 json 格式的字符串进行反序列化的复杂方法
with open('test.json', mode='rt', encoding="utf-8") as f:
    json_res = f.read()
    l = json.loads(json_res)
    print(l, type(l))

# json 验证
# json 格式兼容的是所有语言通用的数据类型，不能识别某一语言的特有类型
# json.dumps({1, 2, 3, 4, 5})
json.loads('[1, "aaa", true, false]')

# 3.5 不支持
l = json.loads(b'[1, "aaa", true, false]')
print(l, type(l))

# with open("test.json", mode='rb') as f:
#     l = json.load(f)

res = json.dumps({'name': '哈哈哈'})
print(res, type(res))

res = json.loads('{"name": "\u54c8\u54c8\u54c8"}')
print(res, type(res))

res = json.loads(b'{"name": "\u54c8\u54c8\u54c8"}')
print(res, type(res))



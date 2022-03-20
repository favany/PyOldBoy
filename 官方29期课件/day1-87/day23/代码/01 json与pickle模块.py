"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""

# 1、什么是序列化&反序列化
#   内存中的数据类型---->序列化---->特定的格式（json格式或者pickle格式）
#   内存中的数据类型<----反序列化<----特定的格式（json格式或者pickle格式）

#   土办法：
#   {'aaa':111}--->序列化str({'aaa':111})----->"{'aaa':111}"
#   {'aaa':111}<---反序列化eval("{'aaa':111}")<-----"{'aaa':111}"

# 2、为何要序列化
#   序列化得到结果=>特定的格式的内容有两种用途
#   1、可用于存储=》用于存档
#   2、传输给其他平台使用=》跨平台数据交互
#        python                 java
#         列表     特定的格式      数组

#   强调：
#       针对用途1的特定一格式：可是一种专用的格式=》pickle只有python可以识别
#       针对用途2的特定一格式：应该是一种通用、能够被所有语言识别的格式=》json


# 3、如何序列化与反序列化
# 示范1
# import json
# # 序列化
# json_res=json.dumps([1,'aaa',True,False])
# # print(json_res,type(json_res)) # "[1, "aaa", true, false]"
#
# # 反序列化
# l=json.loads(json_res)
# print(l,type(l))


# 示范2：
import json

# 序列化的结果写入文件的复杂方法
# json_res=json.dumps([1,'aaa',True,False])
# # print(json_res,type(json_res)) # "[1, "aaa", true, false]"
# with open('test.json',mode='wt',encoding='utf-8') as f:
#     f.write(json_res)

# 将序列化的结果写入文件的简单方法
# with open('test.json',mode='wt',encoding='utf-8') as f:
#     json.dump([1,'aaa',True,False],f)


# 从文件读取json格式的字符串进行反序列化操作的复杂方法
# with open('test.json',mode='rt',encoding='utf-8') as f:
#     json_res=f.read()
#     l=json.loads(json_res)
#     print(l,type(l))

# 从文件读取json格式的字符串进行反序列化操作的简单方法
# with open('test.json',mode='rt',encoding='utf-8') as f:
#     l=json.load(f)
#     print(l,type(l))


# json验证: json格式兼容的是所有语言通用的数据类型，不能识别某一语言的所独有的类型
# json.dumps({1,2,3,4,5})

# json强调：一定要搞清楚json格式，不要与python混淆
# l=json.loads('[1, "aaa", true, false]')
# l=json.loads("[1,1.3,true,'aaa', true, false]")
# print(l[0])

# 了解
# l = json.loads(b'[1, "aaa", true, false]')
# print(l, type(l))

# with open('test.json',mode='rb') as f:
#     l=json.load(f)


# res=json.dumps({'name':'哈哈哈'})
# print(res,type(res))

# res=json.loads('{"name": "\u54c8\u54c8\u54c8"}')
# print(res,type(res))

# 4、猴子补丁
# 在入口处打猴子补丁
# import json
# import ujson
#
# def monkey_patch_json():
#     json.__name__ = 'ujson'
#     json.dumps = ujson.dumps
#     json.loads = ujson.loads
#
# monkey_patch_json() # 在入口文件出运行


# import ujson as json # 不行

# 后续代码中的应用
# json.dumps()
# json.dumps()
# json.dumps()
# json.dumps()
# json.dumps()
# json.dumps()
# json.dumps()
# json.dumps()
# json.loads()
# json.loads()
# json.loads()
# json.loads()
# json.loads()
# json.loads()
# json.loads()
# json.loads()
# json.loads()
# json.loads()
# json.loads()



# 5.pickle模块
import pickle
# res=pickle.dumps({1,2,3,4,5})
# print(res,type(res))

# s=pickle.loads(res)
# print(s,type(s))




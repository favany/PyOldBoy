"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""

# print(abs(-1))
# print(all([1,'aaa','1']))
# print(all([]))

# print(any([0,None,1]))
# print(any([]))

# print(bin(11))
# print(oct(11))
# print(hex(11))

# print(bool(''))

# def func():
#     pass
# class Foo:
#     pass
# print(callable(Foo)) # 方

# print(chr(65))
# print(ord('A'))

# 不可变集合
# s=frozenset({1,2,3})

# hash(不可变类型)

# print(round(1.5))
# print(round(1.4))


# 10 ** 2 % 3
# print(pow(10,2,3))
# s=slice(1,4,2)
# l1=['a','b','c','d','e']
# l2=['aaa','bbb','ccc','ddd',444]
#
# print(l1[1:4:2]) # l1[s]
# print(l2[1:4:2]) # l2[s]


# =================》掌握
# v1='hello'
# v2=[111,222,333,444,5555,6666]
# res=zip(v1,v2)
# print(list(res))

# =================》掌握
# print(divmod(10000,33))

# =================》掌握
# class Foo:
#     pass
# obj=Foo()
# obj.xxx=1111
# print(dir(obj)) # obj.哪些属性

# =================》掌握
# for i,v in enumerate(['a','b','c']):
#     print(i,v)

# =================》掌握
# res=eval('{"a":1}') # 执行字符串中的表达式
# print(res,type(res))


# =================》掌握
# class Foo:
#     pass
# obj=Foo()
# print(isinstance(obj,Foo))
# print(isinstance([],list)) # 类型判断推荐使用isinstance
# print(type([]) is list) # 不推荐使用

# =================》掌握
# import 'time' # 错误
time=__import__('time')
time.sleep(3)

# 下个周：反射
# setattr
# getattr
# delattr
# hasattr




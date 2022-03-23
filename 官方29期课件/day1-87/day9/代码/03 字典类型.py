#1、作用

#2、定义：{}内用逗号分隔开多个key：value，其中value可以使任意类型，但是
#                                   key必须是不可变类型,且不能重复
# 造字典的方式一：
# d={'k1':111,(1,2,3):222} # d=dict(...)
# print(d['k1'])
# print(d[(1,2,3)])
# print(type(d))

# d={} # 默认定义出来的是空字典
# print(d,type(d))

# 造字典的方式二：
# d=dict(x=1,y=2,z=3)
# print(d,type(d))


#3、数据类型转换
# info=[
#     ['name','egon'],
#     ('age',18),
#     ['gender','male']
# ]
# # d={}
# # for k,v in info: # k,v=['name','egon'],
# #     d[k]=v
# # print(d)
#
# 造字典的方式三：
# res=dict(info) # 一行代码搞定上述for循环的工作
# print(res)


# 造字典的方式四:快速初始化一个字典
# keys=['name','age','gender']
# # d={}
# # for k in keys:
# #     d[k]=None
# # print(d)
# d={}.fromkeys(keys,None) # 一行代码搞定上述for循环的工作
# print(d)

#4、内置方法
#优先掌握的操作：
#1、按key存取值：可存可取
# d={'k1':111}
# 针对赋值操作：key存在，则修改
# d['k1']=222
# 针对赋值操作：key不存在，则创建新值
# d['k2']=3333
# print(d)

#2、长度len
# d={'k1':111,'k2':2222,'k1':3333,'k1':4444}
# print(d)
# print(len(d))


#3、成员运算in和not in:根据key
# d={'k1':111,'k2':2222}
# print('k1' in d)
# print(111 in d)

#4、删除
d={'k1':111,'k2':2222}
# 4.1 通用删除
# del d['k1']
# print(d)

# 4.2 pop删除：根据key删除元素，返回删除key对应的那个value值
# res=d.pop('k2')
# print(d)
# print(res)

# 4.3 popitem删除：随机删除，返回元组(删除的key,删除的value)
# res=d.popitem()
# print(d)
# print(res)

#5、键keys()，值values()，键值对items()  =>在python3中得到的是老母鸡
d={'k1':111,'k2':2222}
'''
在python2中
>>> d={'k1':111,'k2':2222}
>>> 
>>> d.keys()#6、循环
['k2', 'k1']
>>> d.values()
[2222, 111]
>>> d.items()
[('k2', 2222), ('k1', 111)]
>>> dict(d.items())
{'k2': 2222, 'k1': 111}
>>>
'''  

#6、for循环
# for k in d.keys():
#     print(k)
#
# for k in d:
#     print(k)

# for v in d.values():
#     print(v)

# for k,v in d.items():
#     print(k,v)


# print(list(d.keys()))
# print(list(d.values()))
# print(list(d.items()))


#需要掌握的内置方法
d={'k1':111}
#1、d.clear()

#2、d.update()
# d.update({'k2':222,'k3':333,'k1':111111111111111})
# print(d)

#3、d.get() ：根据key取值，容错性好
# print(d['k2'])  # key不存在则报错

# print(d.get('k1')) # 111
# print(d.get('k2')) # key不存在不报错，返回None

#4、d.setdefault()
# info={}
# if 'name' in info:
#     ... # 等同于pass
# else:
#     info['name']='egon'
# print(info)

# 4.1 如果key有则不添加,返回字典中key对应的值
info={'name':'egon'}
res=info.setdefault('name','egon')
# print(info)

print(res)

# 4.2 如果key没有则添加，返回字典中key对应的值
info={}
res=info.setdefault('name','egon')
# print(info)
print(res)

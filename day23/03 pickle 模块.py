# @File      : 03 pickle 模块
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/6/2 10:30 AM
# @Info      :

import pickle

res = pickle.dumps({1, 2, 3})
print(res, type(res))

s = pickle.loads(res)
print(s, type(s))

# pickle 在python2 和 python3 中有兼容性问题


# shelve模块
# shelve模块 比 pickle 模块简单，只有一个open函数，返回类似字典的对象，可读可写；key必须为字符
# 可以是python所支持的数据类型

# import shelve
# f=shelve.open(r'sheve.txt')
# f['stul info']={'name':'egon','age':18,'hobby':['smoking','drinking']
# f['stu2 info']={'name':'gangdan','age':53}
# f['school info']={'website':'http://www.pypy.org','city':'beijing'}
# print (f['stul info']['hobby']

# f.close()


# xml 模块： json之前的语言之间数据交换的协议

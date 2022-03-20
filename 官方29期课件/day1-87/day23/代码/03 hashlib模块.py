"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""
# 1、什么是哈希hash
#    hash一类算法，该算法接受传入的内容，经过运算得到一串hash值
#    hash值的特点：
#I 只要传入的内容一样，得到的hash值必然一样
#II 不能由hash值返解成内容
#III 不管传入的内容有多大，只要使用的hash算法不变，得到的hash值长度是一定

# 2、hash的用途
# 用途1：特点II用于密码密文传输与验证
# 用途2：特点I、III用于文件完整性校验

# 3、如何用
# import hashlib
#
# m=hashlib.md5()
# m.update('hello'.encode('utf-8'))
# m.update('world'.encode('utf-8'))
# res=m.hexdigest() # 'helloworld'
# print(res)
#
# m1=hashlib.md5('he'.encode('utf-8'))
# m1.update('llo'.encode('utf-8'))
# m1.update('w'.encode('utf-8'))
# m1.update('orld'.encode('utf-8'))
# res=m1.hexdigest()# 'helloworld'
# print(res)



# 模拟撞库
# cryptograph='aee949757a2e698417463d47acac93df'
# import hashlib
#
# # 制作密码字段
# passwds=[
#     'alex3714',
#     'alex1313',
#     'alex94139413',
#     'alex123456',
#     '123456alex',
#     'a123lex',
# ]
#
# dic={}
# for p in passwds:
#     res=hashlib.md5(p.encode('utf-8'))
#     dic[p]=res.hexdigest()
#
# # 模拟撞库得到密码
# for k,v in dic.items():
#     if v == cryptograph:
#         print('撞库成功，明文密码是：%s' %k)
#         break


# 提升撞库的成本=>密码加盐
import hashlib

m=hashlib.md5()

m.update('天王'.encode('utf-8'))
m.update('alex3714'.encode('utf-8'))
m.update('盖地虎'.encode('utf-8'))
print(m.hexdigest())









# m.update(文件所有的内容)
# m.hexdigest()
#
# f=open('a.txt',mode='rb')
# f.seek()
# f.read(2000) # 巨琳
# m1.update(文见的一行)
#
# m1.hexdigest()






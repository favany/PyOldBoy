# @File      : 05 hash 和 hashlib模块
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/6/2 1:19 PM
# @Info      :

# 什么是哈希 hash ？
# hash 一类算法，该算法接收传入的内容，经过运算得到一串 hash 值

# hash 值的特点：
# 1. 传给它的内容一样，得到的结果一定一样 明文传输密码文件完整性校验
# 2. 不能由 hash 值反解出内容 用于密码密文的传输与验证
# 3. 只要使用的 hash 算法不变，无论校验的内容多大，得到hash值的长度是固定的 文件完整性校验


# hash 的用途:
# 用途1 用于密码密文传输与验证
# 123455 ==> 字符串
# 用途2 用于文件完整性校验
# 客户端 ==> （加密🔐）hash 字符串 ===> 服务端（与存储的hash字符串进行比对）

import hashlib

m = hashlib.md5()  # 哈希工厂
m.update('hello'.encode("utf-8"))  # 传入bytes类型
m.update('world'.encode("utf-8"))
res = m.hexdigest() # "helloworld"的校验结果
print(res)

m1 = hashlib.md5('he'.encode('utf-8'))
m1.update('llo'.encode('utf-8'))
m1.update('world'.encode('utf-8'))
res1 = m.hexdigest()  # "helloworld"的校验结果
print(res1)

# 文件推荐逐行读取，否则可能会内存溢出
# m.update(文件的一行) ...
# m1.hexdigest()

# f = open('a.txt', mode="rb")
# f.seek()
# f.read(2000)
# m1.update(文件的一行)

# 模拟撞库
cryptograph = 'fc5e038d38a57032085441e7fe7010b0'
pwds = ['1234', '123456', '12345678', '123']

import hashlib
dic = {}
for p in pwds:
    res = hashlib.md5(p.encode('utf-8'))
    dic[p] = res.hexdigest()

print(dic)
for k,v in dic.items():
    if v == cryptograph:
        print('撞库成功，明文密码是：%s' % k)
        break

# 提升撞库的成本：密码加盐
import hashlib
# 'al' '天王' 'ex' '盖地虎' '1234'
m = hashlib.md5()
m.update('al'.encode('utf-8'))
m.update('天王'.encode('utf-8'))
m.update('ex'.encode('utf-8'))
m.update('盖地虎'.encode('utf-8'))
m.update('1234'.encode('utf-8'))






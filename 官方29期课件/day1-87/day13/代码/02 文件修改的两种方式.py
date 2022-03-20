"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""

# with open('a.txt',mode='r+t',encoding='utf-8') as f:
#     f.seek(9,0)
#     f.write('<男妇女主任>')


# 文件修改的两种方式
# 方式一：文本编辑采用的就是这种方式
# 实现思路：将文件内容发一次性全部读入内存,然后在内存中修改完毕后再覆盖写回原文件
# 优点: 在文件修改过程中同一份数据只有一份
# 缺点: 会过多地占用内存
# with open('c.txt',mode='rt',encoding='utf-8') as f:
#     res=f.read()
#     data=res.replace('alex','dsb')
#     print(data)
#
# with open('c.txt',mode='wt',encoding='utf-8') as f1:
#     f1.write(data)


# 方式二：
import os
# 实现思路：以读的方式打开原文件,以写的方式打开一个临时文件,一行行读取原文件内容,修改完后写入临时文件...,删掉原文件,将临时文件重命名原文件名
# 优点: 不会占用过多的内存
# 缺点: 在文件修改过程中同一份数据存了两份
with open('c.txt', mode='rt', encoding='utf-8') as f, \
        open('.c.txt.swap', mode='wt', encoding='utf-8') as f1:
    for line in f:
        f1.write(line.replace('alex', 'dsb'))

os.remove('c.txt')
os.rename('.c.txt.swap', 'c.txt')




f = open('a.txt')
res = f.read()
print(res)

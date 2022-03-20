"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""

# 1、打开文件
# windows路径分隔符问题
# open('C:\a.txt\nb\c\d.txt')
# 解决方案一：推荐
# open(r'C:\a.txt\nb\c\d.txt')
# 解决方案二：
# open('C:/a.txt/nb/c/d.txt')


f=open(r'aaa/a.txt',mode='rt') # f的值是一种变量，占用的是应用程序的内存空间
# print(f)
# x=int(10)

# 2、操作文件：读/写文件，应用程序对文件的读写请求都是在向操作系统发送
# 系统调用，然后由操作系统控制硬盘把输入读入内存、或者写入硬盘
res=f.read()
print(type(res))
# print(res)
# 3、关闭文件
f.close() # 回收操作系统资源
# print(f)
# f.read() # 变量f存在，但是不能再读了

# del f     # 回收应用程序资源










# @File      : 01 文件操作基本
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/6/9 4:04 PM
# @Info      :

# 1. 打开文件

# open(r'C:\a\b\c\d.txt') # raw string
# open('C:/a/b/c/d.txt')

f = open(r'path/a.txt', mode="rt")  # 数据类型：文件类型 f的值是一种变量，占用的是应用程序的内存空间
# f 是文件对象，也称为文件句柄
print(f)

# 2. 操作文件：读 / 写文件
# 应用程序对文件的读写请求都是在向操作系统发送系统调用，然后由操作系统控制硬盘把数据读入内存，或者写入硬盘.

res = f.read()
print(res)

# 3. 关闭文件

f.close()  # 回收操作系统资源 需要关闭


print(f)  # 变量 f 存在，但是不能再读了
# f.read()  # ValueError: I/O operation on closed file.
# del f  # 回收应用程序资源






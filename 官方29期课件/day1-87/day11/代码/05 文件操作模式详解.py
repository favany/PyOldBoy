"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""
# 以t模式为基础进行内存操作

# 1、r（默认的操作模式）：只读模式，当文件不存在时报错，当文件存在时文件指针跳到开始位置
# with open('c.txt',mode='rt',encoding='utf-8') as f:
#     print('第一次读'.center(50,'*'))
#     res=f.read() # 把所有内容从硬盘读入内存
#     print(res)
#
# # with open('c.txt', mode='rt', encoding='utf-8') as f:
#     print('第二次读'.center(50,'*'))
#     res1=f.read()
#     print(res1)


# ===============案例==================
# inp_username=input('your name>>: ').strip()
# inp_password=input('your password>>: ').strip()
#
# # 验证
# with open('user.txt',mode='rt',encoding='utf-8') as f:
#     for line in f:
#         # print(line,end='') # egon:123\n
#         username,password=line.strip().split(':')
#         if inp_username == username and inp_password == password:
#             print('login successfull')
#             break
#     else:
#         print('账号或密码错误')


# 应用程序====》文件
# 应用程序====》数据库管理软件=====》文件

# 2、w：只写模式，当文件不存在时会创建空文件，当文件存在会清空文件，指针位于开始位置
# with open('d.txt',mode='wt',encoding='utf-8') as f:
    # f.read() # 报错，不可读
    # f.write('擦勒\n')

# 强调1：
# 在以w模式打开文件没有关闭的情况下，连续写入，新的内容总是跟在旧的之后
# with open('d.txt',mode='wt',encoding='utf-8') as f:
#     f.write('擦勒1\n')
#     f.write('擦勒2\n')
#     f.write('擦勒3\n')

# 强调2：
# 如果重新以w模式打开文件，则会清空文件内容
# with open('d.txt',mode='wt',encoding='utf-8') as f:
#     f.write('擦勒1\n')
# with open('d.txt',mode='wt',encoding='utf-8') as f:
#     f.write('擦勒2\n')
# with open('d.txt',mode='wt',encoding='utf-8') as f:
#     f.write('擦勒3\n')

# 案例：w模式用来创建全新的文件
# 文件文件的copy工具

# src_file=input('源文件路径>>: ').strip()
# dst_file=input('源文件路径>>: ').strip()
# with open(r'{}'.format(src_file),mode='rt',encoding='utf-8') as f1,\
#     open(r'{}'.format(dst_file),mode='wt',encoding='utf-8') as f2:
#     res=f1.read()
#     f2.write(res)


# 3、a：只追加写，在文件不存在时会创建空文档，在文件存在时文件指针会直接调到末尾
# with open('e.txt',mode='at',encoding='utf-8') as f:
#     # f.read() # 报错，不能读
#     f.write('擦嘞1\n')
#     f.write('擦嘞2\n')
#     f.write('擦嘞3\n')

# 强调 w 模式与 a 模式的异同：
# 1 相同点：在打开的文件不关闭的情况下，连续的写入，新写的内容总会跟在前写的内容之后
# 2 不同点：以 a 模式重新打开文件，不会清空原文件内容，会将文件指针直接移动到文件末尾，新写的内容永远写在最后


# 案例：a模式用来在原有的文件内存的基础之上写入新的内容，比如记录日志、注册
# 注册功能
# name=input('your name>>: ')
# pwd=input('your name>>: ')
# with open('db.txt',mode='at',encoding='utf-8') as f:
#     f.write('{}:{}\n'.format(name,pwd))


# 了解：+不能单独使用，必须配合r、w、a
# with open('g.txt',mode='rt+',encoding='utf-8') as f:
#     # print(f.read())
#     f.write('中国')

# with open('g.txt',mode='w+t',encoding='utf-8') as f:
#     f.write('111\n')
#     f.write('222\n')
#     f.write('333\n')
#     print('====>',f.read())

#
# with open('g.txt',mode='a+t',encoding='utf-8') as f:
#     print(f.read())
#
#     f.write('444\n')
#     f.write('5555\n')
#     print(f.read())
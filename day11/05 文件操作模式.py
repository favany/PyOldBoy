# @File      : 05 文件操作模式
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/6/10 3:00 PM
# @Info      :

# 以 t 模式为基准进行操作


# 1. r（默认的操作模式）：只读模式，当文件不存在时报错，当文件存在时，文件指针跳到开始位置
with open('path/c.txt', mode='rt', encoding='utf8') as f:
    # print('第一次读'.center(66, '*'))
    res = f.read()  # 把所有内容从硬盘读到内存
    print(res)

    # print('第二次读'.center(66, '*'))
    # res1 = f.read()
    # print(res1)  # 无内容 第一次读已读完了

# inp_username = input('your name >>:').strip()
# inp_password = input('your password >>:').strip()

# with open('path/user.txt', mode='rt', encoding='utf8') as f:
#     for line in f:
#         username, password = line.strip().split(':')
#         if inp_username == username and inp_password == password:
#             print('login success')
#             break
#     else:
#         print('login failed')

# 2. w：只写模式，当文件不存在时，会创建空文件；当文件存在时，会清空文件，指针位于开始位置。

with open('t.txt', mode='wt', encoding='utf8') as f:
    f.write('666\n')
    # f.read()  # 报错，不可读

"""
强调，
    在以 w 的模式打开文件后，在没有关闭的情况下，可以以多个 f.write() 连续写；
    如果重新打开文件，则会清空文件
"""

# 创建全新的文件

# with open('e.txt', mode='rt', encoding='utf8') as f1, \
#     open('f.txt', mode='wt', encoding='utf8') as f2:
#     res = f1.read()
#     f2.write(res)

# 拷贝文件

src_file = input("源文件路径").strip()
dest_file = input("目标文件路径").strip()
with open(src_file, mode='rt', encoding='utf8') as f1, \
        open(dest_file, mode='wt', encoding='utf8') as f2:
    res = f1.read()
    f2.write(res)

# 3. a：追加写
# 在文件不存在时，会创建空文件；在文件存在时，文件指针会直接跳到末尾。
# 用来在原有的文件内存的基础上，写入新的内容，比如记录日志


with open('e.txt', mode='at', encoding='utf8') as f:
    f.write("")  # 在文件最后追加写
    # f.read()  # 报错，不能读

"""
w 和 a 模式的异同：
相同点： 打开文件不关闭的情况下，连续的写入，新写的内容会跟在前面的内容之后
不同点： w 模式打开文件时会清空文件，而 a 模式打开时不会清空文件，文件指针会跳到末尾。
"""

# 注册功能
name = input("your name >>")
pwd = input("your password >>")
with open('db.txt', mode='wt', encoding='utf8') as f:
    f.write('{}:{}\n'.format(name, pwd))

# 了解可读可写：+ 不能单独使用，必须配合 r w b
# r+t 可读可写（开头写，覆盖原内容） 但是特性是依据 r 的 文件不存在，报错
# w+t 读不出内容
# a+t

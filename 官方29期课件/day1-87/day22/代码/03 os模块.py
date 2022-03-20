"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""

import os

# 获取某一个文件夹下所有的子文件以及子文件夹的名字
# res=os.listdir('.')
# print(res)
#
#
# size=os.path.getsize(r'/Users/linhaifeng/PycharmProjects/s14/day22/01 时间模块.py')
# print(size)



# os.remove()  删除一个文件
# os.rename("oldname","newname")  重命名文件/目录



# 应用程序----》"ls /"
# os.system("ls /")

# 规定：key与value必须都为字符串

# os.environ['aaaaaaaaaa']='111'
# print(os.environ)


# print(os.path.dirname(r'/a/b/c/d.txt'))
# print(os.path.basename(r'/a/b/c/d.txt'))


# print(os.path.isfile(r'笔记.txt'))
# print(os.path.isfile(r'aaa'))
# print(os.path.isdir(r'aaa'))

# print(os.path.join('a','/','b','c','d'))




# 推荐用这种
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# print(BASE_DIR)


# BASE_DIR=os.path.normpath(os.path.join(
#     __file__,
#     '..',
#     '..'
# ))
# print(BASE_DIR)

# 在python3.5之后，推出了一个新的模块pathlib
from pathlib import Path

# res = Path(__file__).parent.parent
# print(res)


# res=Path('/a/b/c') / 'd/e.txt'
# print(res)

# print(res.resolve())


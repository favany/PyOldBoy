"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""
# 无论是import还是from...import在导入模块时都涉及到查找问题
# 优先级：
# 1、内存（内置模块）
# 2、硬盘：按照sys.path中存放的文件的顺序依次查找要导入的模块

# import sys
# 值为一个列表，存放了一系列的对文件夹
# 其中第一个文件夹是当前执行文件所在的文件夹
# print(sys.path)

# import foo # 内存中已经有foo了
# foo.say()
#
# import time
# time.sleep(10)
#
# import foo
# foo.say()


# 了解：sys.modules查看已经加载到内存中的模块
import sys
# import foo # foo=模块的内存地址
# del foo

# def func():
#     import foo # foo=模块的内存地址
#
# func()
#
# # print('foo' in sys.modules)
# print(sys.modules)


import sys
# 找foo.py就把foo.py的文件夹添加到环境变量中
sys.path.append(r'/Users/linhaifeng/PycharmProjects/s14/day21/aa')
# import foo
# foo.say()

from foo import say








"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""

# # 绝对导入======>sys.path====>执行文件
# import sys
# # sys.path.append(r'/Users/linhaifeng/PycharmProjects/s14/day21/ATM')
#
# # from conf import settings
# # from core import src
# # from db import db_handle
# # from lib import common
#
# # print(settings)
# # print(src)
#
# from core import src
# # src.run()
#
# # from core.src import run
# # run()


# 优化方案
import os
import sys

# print(__file__) # 当前文件的绝对路径
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from core import src

if __name__ == '__main__':
    src.run()


"""
@Time    : 2022/7/4 11:26
@Author  : 刘俊 jun.liu@deepfinance.com
@File    : start.py
"""

# 绝对导入 ==> sys.path  ==> 执行文件
import sys
# 把项目的根目录加到环境变量中
sys.path.append('/Users/admin/Projects/PyOldBoy/ATM')

# from conf import  settings
# from core import src
# from db imoprt

# 优化方案

import os
import sys

# print(__file__)  # 当前文件的绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# from core import src

if __name__ == '__main__':
    src.run()

'''
程序的入口
'''
import sys
import os

# 添加解释器的环境变量
sys.path.append(
    os.path.dirname(__file__)
)

from core import src

# 开始执行项目函数
if __name__ == '__main__':

    # 1、先执行用户视图层
    src.run()


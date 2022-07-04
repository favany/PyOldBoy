"""
@File      : 03 模块的搜索路径优先级.py
@Author    : 刘俊 mophia
@Email     : faaa@live.com
@Time      : 2022/7/2 1:04 PM

无论是 import 还是 from ... import 在导入模块时，都涉及到模块查找优先级的问题

优先级：
1. 内存（内置模块、以及之前导入过的模块会缓存在内存中）
2. 从硬盘找（文件夹）
"""

import sys

print(sys.path)
'''
sys.path 的值是一个列表，存放了一系列的文件夹
其中第一个文件夹是当前执行文件所在的文件夹（很重要）

['/Users/admin/Projects/PyOldBoy/day21', '/Applications/PyCharm.app/Contents/plugins/python/helpers/pydev', 
'/Users/admin/Projects/PyOldBoy', '/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_display', 
'/Applications/PyCharm.app/Contents/plugins/python/helpers/third_party/thriftpy', 
'/Applications/PyCharm.app/Contents/plugins/python/helpers/pydev', 
'/Users/admin/Library/Caches/JetBrains/PyCharm2021.3/cythonExtensions', '/Users/admin/Projects/PyOldBoy/day21', 
'/Library/Frameworks/Python.framework/Versions/3.10/lib/python310.zip', 
'/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10', 
'/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/lib-dynload', 
'/Users/admin/Projects/PyOldBoy/venv/lib/python3.10/site-packages', 
'/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_matplotlib_backend']
 '''


import aa.foo as foo
foo.say()

import time
time.sleep(10)

import aa.foo as foo
foo.say()


del foo  # 不会删除，会保留 foo 的内存空间
print(sys.modules)


import sys
# 把 foo.py 的文件夹添加到环境变量中
sys.path.append('/Users/admin/Projects/PyOldBoy/day21/aa')
import foo
foo.say()




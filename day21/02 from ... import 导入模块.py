
'''
import 导入模块，在使用时，必须加前缀 "模块."

- 优点：肯定不会与当前名称空间中的名字冲突
- 缺点：加前缀显得麻烦


from ... import ...

导入也发生三件事

- 产生一个模块的名称空间
- 运行 foo.py 将运行过程中产生的名字都加到模块的名称空间中
- 在当前名称空间拿到一个名字，该名字与模块名称空间中的同一个名字指向某一个内存地址

- 优点：代码更精简
- 缺点：容易与当前的名称空间混淆
'''


# 一行导入多个名字（不推荐）

from foo import x
from foo import get
from foo import change


from foo import *

'''
* 导入模块中的所有名字
__all__ = ['a', 'b', 'c']
控制 * 中导入的名字

import b as 别名 
from a as b as b的别名
'''
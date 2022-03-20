# 绝对导入，以包的文件夹作为起始来进行导入
# # import sys
# # print('==========>这是在被导入的__init__.py中查看到的sys.path')
# # print(sys.path)
#
#
# from foo.m1 import f1
# from foo.m2 import f2
# from foo.m3 import f3
#
# from foo.bbb.m4 import f4 # foo内有了一个f4
# # import foo.bbb.m4.f4 # 语法错误，点的左侧必须是一个包


# 相对导入:仅限于包内使用，不能跨出包（包内模块之间的导入，推荐使用相对导入）
# .:代表当前文件夹
# ..:代表上一层文件夹

from .m1 import f1
from .m2 import f2
from .m3 import f3
from .bbb.m4 import f4
# 强调：
# 1、相对导入不能跨出包，所以相对导入仅限于包内模板彼此之间闹着玩

# 而绝对导入是没有任何限制的，所以绝对导入是一种通用的导入方式
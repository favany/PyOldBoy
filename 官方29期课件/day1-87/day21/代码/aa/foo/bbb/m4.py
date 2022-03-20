# from foo.m1 import f1
from ..m1 import f1

# 绝对导入f5
# from foo.bbb.m5 import f5
# 相对导入f5
from .m5 import f5

def f4():
    print('功能f4...')
    f1()
    f5()
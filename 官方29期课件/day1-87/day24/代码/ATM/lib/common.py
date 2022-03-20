"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""

import time
from conf import settings

def logger(msg):
    with open(settings.LOG_PATH,mode='at',encoding='utf-8') as f:
        f.write('%s %s\n' %(time.strftime('%Y-%m-%d %H:%M:%S'),msg))

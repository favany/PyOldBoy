"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""
# 课后了解性质——》闲着没事自己研究下
# import logging.config
#
# logging.config.dictConfig(settings.LOGGING_DIC)
# print(logging.getLogger)

# 接下来要做的是：拿到日志的产生者即loggers来产生日志
# 第一个日志的产生者：kkk
# 第二个日志的产生者：bbb

# 但是需要先导入日志配置字典LOGGING_DIC
import settings
from logging import config,getLogger

config.dictConfig(settings.LOGGING_DIC)


# logger1=getLogger('kkk')
# logger1.info('这是一条info日志')

# logger2=getLogger('终端提示')
# logger2.info('logger2产生的info日志')

# logger3=getLogger('用户交易')
# logger3.info('logger3产生的info日志')

logger4=getLogger('用户常规')
logger4.info('logger4产生的info日志')

# 补充两个重要额知识
# 1、日志名的命名
#    日志名是区别日志业务归属的一种非常重要的标识

# 2、日志轮转
#    日志记录着程序员运行过程中的关键信息




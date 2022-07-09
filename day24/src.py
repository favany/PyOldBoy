"""
@File      : src.py
@Author    : 刘俊 mophia
@Email     : faaa@live.com
@Time      : 2022/7/9 9:23 AM
"""

# 拿到日志的产生者，即 loggers (1. default 2. other) 来产生日志
# 但需要先导入日志的配置

import settings
from logging import config, getLogger

config.dictConfig(settings.LOGGING_DIC)

# logger1 = getLogger('用户交易')
# logger1.info('这是日志')

# logger2 = getLogger('终端提示')
# logger2.info('这是日志')

logger3 = getLogger('测试日志')
logger3.info('这是日志')

# 日志轮转



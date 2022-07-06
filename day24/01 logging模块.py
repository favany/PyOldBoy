"""
@File      : 01 logging模块.py
@Author    : 刘俊 mophia
@Email     : faaa@live.com
@Time      : 2022/6/5 10:58 AM
"""

import logging

logging.basicConfig(
    # 1、日志输出位置：终端或文件 filename="" 不指定，默认打印到终端
    filename='access.log',
    # 2、日志格式
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    # 3、时间格式
    datefmt='%Y-%m-%d %H:%M:%S %p',
    # 4、日志级别 critical 50； error 40; warning 30；info 20；debug 10
    level=10)


logging.debug('调试debug')
logging.info('消息info')
logging.warning('警告⚠️warning')
logging.error('错误error')
logging.critical('严重critical')

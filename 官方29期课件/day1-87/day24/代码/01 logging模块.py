"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""

import logging

logging.basicConfig(
    # 1、日志输出位置：1、终端 2、文件
    filename='access.log', # 不指定，默认打印到终端

    # 2、日志格式
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',

    # 3、时间格式
    datefmt='%Y-%m-%d %H:%M:%S %p',

    # 4、日志级别
    # critical => 50
    # error => 40
    # warning => 30
    # info => 20
    # debug => 10
    level=10,
)

logging.debug('调试debug') # 10
logging.info('消息info')   # 20
logging.warning('警告warn')# 30
logging.error('egon提现失败') # 40
logging.critical('严重critical') # 50






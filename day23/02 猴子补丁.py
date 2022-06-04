# @File      : 02 猴子补丁
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/6/2 9:14 AM
# @Info      :

# 猴子补丁
# 用自己的代码替换所用模块的源代码 说明这部分不是原装的
# 在入口文件改，所有文件都能使用

import json
import ujson


def monkey_patch_json():
    json.__name__ = 'ujson'
    json.dumps = ujson.dumps
    json.loads = ujson.loads


monkey_patch_json() # 在入口文件运行

# import ujson as json

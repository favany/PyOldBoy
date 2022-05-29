# @File      : 01 时间模块
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/5/28 3:35 PM
# @Info      :

# 时间模块优先掌握的操作

# 一、time
# 1. 时间戳：从1970年到现在经历的秒数
#    作用：用于时间间隔的计算
import time
import datetime

print(time.time())  # 1653723496.210679

# 2. 格式化的字符串形式的时间：2020-03-30 11:11:11
print(time.strftime('%Y-%m-%d %H:%M:%S %p'))
print(time.strftime('%Y-%m-%d %X'))

# 3、结构化时间
#     作用：用于单独获取时间的一部分
local_time = time.localtime()
print("local time is:", local_time)

# 今年
print(local_time.tm_year)
# 今年的第几天
print(local_time.tm_yday)

# 二、datetime
print(datetime.datetime.now())
print(datetime.datetime.now() + datetime.timedelta(days=3))  # 计算三天后的时间
print(datetime.datetime.now() + datetime.timedelta(weeks=1))  # 计算一年后的时间


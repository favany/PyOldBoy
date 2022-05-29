# @File      : 02 时间转换
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/5/28 4:14 PM
# @Info      :
import datetime
import time

# 时间模块需要掌握的操作

# 1、时间格式的转换
# i. 结构化时间 与 时间戳
# 生成结构化的时间
struct_time = time.localtime()
print("struct time:", struct_time)

# 结构化时间 -> 时间戳
timestamp = time.mktime(struct_time)
print("timestamp:", timestamp)

# 时间戳 -> 结构化时间
timestamp = time.time()
struct_time = time.localtime(timestamp)
print("struct time:", struct_time)

# 格林尼治时间
print(time.gmtime())
print(time.gmtime(timestamp))

# ii. 结构化时间 与 字符串形式的时间
# 结构化时间 -> 字符串形式的时间
struct_time = time.localtime()

string_time = time.strftime("%Y-%m-%d %H:%M:%S", struct_time) # struct_time 是默认值
print(string_time)

# 字符串形式的时间 -> 结构化时间
struct_time = time.strptime(string_time, "%Y-%m-%d %H:%M:%S")
print(struct_time)

# 真正需要掌握的

# "1988-03-03 11:11:11" + 7天
# 字符串时间 -> 结构化时间 -> 时间戳
struct_time = time.strptime("1988-03-03 11:11:11", "%Y-%m-%d %H:%M:%S")
timestamp = time.mktime(struct_time) + 7*86400

# 时间戳 -> 结构化时间 -> 字符串时间
time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))

# 了解

# Linux 时间 'Sat Jun 06 16:26:11 1998' time.asctime()

print("utc time", datetime.datetime.utcnow())
print("time", datetime.datetime.now())

# 时间戳 -> 字符串时间
print(datetime.datetime.fromtimestamp(timestamp))

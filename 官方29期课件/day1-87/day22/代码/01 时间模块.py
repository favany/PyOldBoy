"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""
# 时间模块优先掌握的操作
#一：time
import time

# 时间分为三种格式：
# 1、时间戳：从1970年到现在经过的秒数
#    作用：用于时间间隔的计算

# print(time.time())

# 2、按照某种格式显示的时间：2020-03-30 11:11:11
#    作用：用于展示时间

# print(time.strftime('%Y-%m-%d %H:%M:%S %p'))
# print(time.strftime('%Y-%m-%d %X'))

# 3、结构化的时间
#    作用：用于单独获取时间的某一部分

# res=time.localtime()
# print(res)
# print(res.tm_year)
# print(res.tm_yday)

#二：datetime
import datetime

# print(datetime.datetime.now())
# print(datetime.datetime.now() + datetime.timedelta(days=3))
# print(datetime.datetime.now() + datetime.timedelta(weeks=1))



# 时间模块需要掌握的操作
# 1、时间格式的转换
# struct_time->时间戳
import time
# s_time=time.localtime()
# print(time.mktime(s_time))

# 时间戳->struct_time
# tp_time=time.time()
# print(time.localtime(tp_time))

# 补充：世界标准时间与本地时间
# print(time.localtime())
# print(time.gmtime()) # 世界标准时间，了解
# print(time.localtime(333333333))
# print(time.gmtime(333333333))


# struct_time->格式化的字符串形式的时间
# s_time=time.localtime()
# print(time.strftime('%Y-%m-%d %H:%M:%S',s_time))

# print(time.strptime('1988-03-03 11:11:11','%Y-%m-%d %H:%M:%S'))


# !!!真正需要掌握的只有一条：format string<------>timestamp
# '1988-03-03 11:11:11'+7

# format string--->struct_time--->timestamp
# struct_time=time.strptime('1988-03-03 11:11:11','%Y-%m-%d %H:%M:%S')
# timestamp=time.mktime(struct_time)+7*86400
# print(timestamp)

# format string<---struct_time<---timestamp
# res=time.strftime('%Y-%m-%d %X',time.localtime(timestamp))
# print(res)

# time.sleep(3)

# 了解知识
# import time
# print(time.asctime())


import datetime
# print(datetime.datetime.now())
# print(datetime.datetime.utcnow())

print(datetime.datetime.fromtimestamp(333333))






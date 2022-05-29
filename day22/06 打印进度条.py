# @File      : 06 打印进度条.py
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/5/29 11:45 AM
# @Info      :
import time


def progress(percentage):
    if percentage > 1:
        percentage = 1
    Str = '#' * int(25 * percentage)
    # 左对齐，指定宽度为 25
    # \r: 不换行，每次打印都从行首开始打印
    print('\r下载中：[%-25s] %d%%' % (Str, 100*percentage), end="")


receive_size = 0
total_size = 100000

while receive_size < total_size:
    time.sleep(0.4)
    receive_size += 5048
    per = receive_size / total_size
    progress(per)

print('\r下载成功！')

"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""
import time

with open('access.log', mode='rb') as f:
    # 1、将指针跳到文件末尾
    # f.read() # 错误
    f.seek(0,2)

    while True:
        line=f.readline()
        if len(line) == 0:
            time.sleep(0.3)
        else:
            print(line.decode('utf-8'),end='')

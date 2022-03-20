"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""

with open('a.txt', mode='rt', encoding='utf-8') as f:
    for line in f:
        print(line)
    print('=====================')
    while True:
        # line=f.read(1024)
        line = f.readline()
        print(line)
        if len(line) == 0:
            break

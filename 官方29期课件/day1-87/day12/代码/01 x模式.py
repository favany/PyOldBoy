"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128


x模式（控制文件操作的模式）-》了解
    x， 只写模式【不可读；不存在则创建，存在则报错】
"""
# with open('a.txt',mode='x',encoding='utf-8') as f:
#     pass

# with open('c.txt',mode='x',encoding='utf-8') as f:
#     f.read()

with open('d.txt', mode='x', encoding='utf-8') as f:
    f.write('哈哈哈\n')














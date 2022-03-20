"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""

'''
强调：t和b不能单独使用，必须跟r/w/a连用

t文本（默认的模式）
1、读写都以str（unicode）为单位的
2、文本文件
3、必须指定encoding='utf-8'

'''
# 没有指定encoding参数操作系统会使用自己默认的编码
# linux系统默认utf-8
# windows系统默认gbk
with open('c.txt',mode='rt',encoding='utf-8') as f:
    res=f.read() # t模式会将f.read()读出的结果解码成unicode
    print(res,type(res))



# 内存：utf-8格式的二进制-----解码-----》unicode
# 硬盘（c.txt内容：utf-8格式的二进制）






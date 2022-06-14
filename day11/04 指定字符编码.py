# @File      : 04 指定字符编码
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/6/9 5:18 PM
# @Info      :

"""
强调：t 和 b 不能单独使用，必须和 r / w / a 连用

t 文本（默认的模式）
1、读写都以 str（unicode）为单位
2、文本文件
3、必须指定 encoding = 'utf-8'

"""

# 没有指定 encoding 参数，操作系统会使用自己默认的编码
# linux 默认 utf-8
# windows 默认 jbk

with open('path/c.txt', mode='rt', encoding='utf8') as f:
    res = f.read()  # t 模式会将 f.read() 读出的结果解码成 unicode
    print(res, type(res))

# 内存：utf-8 格式的二进制 --> 解码 --> unicode

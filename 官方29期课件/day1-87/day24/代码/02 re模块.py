"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""
import re

# print(re.findall('\w','aAbc123_*()-='))
# print(re.findall('\W','aAbc123_*()-= '))
# print(re.findall('\s','aA\rbc\t\n12\f3_*()-= '))
# print(re.findall('\S','aA\rbc\t\n12\f3_*()-= '))
# print(re.findall('\d','aA\rbc\t\n12\f3_*()-= '))
# print(re.findall('\D','aA\rbc\t\n12\f3_*()-= '))
# print(re.findall('\D','aA\rbc\t\n12\f3_*()-= '))
# print(re.findall('\Aalex',' alexis alex sb'))
#                          alex
# print(re.findall('sb\Z',' alexis alexsb sb'))
#                                       sb\Z
# print(re.findall('sb\Z',"""alex
# alexis
# alex
# sb
# """))

# print(re.findall('^alex','alexis alex sb'))
# print(re.findall('sb$','alexis alex sb'))
# print(re.findall('sb$',"""alex
# alexis
# alex
# sb
# """))

# print(re.findall('^alex$','alexis alex sb'))
# print(re.findall('^alex$','al       ex'))
# print(re.findall('^alex$','alex'))

# 重复匹配：| . | * | ? | .* | .*? | + | {n,m} |
# 1、.:匹配除了\n之外任意一个字符，指定re.DOTALL之后才能匹配换行符
# print(re.findall('a.b','a1b a2b a b abbbb a\nb a\tb a*b'))
#                                                   a.b
# ['a1b','a2b','a b','abb','a\tb','a*b']
# print(re.findall('a.b','a1b a2b a b abbbb a\nb a\tb a*b',re.DOTALL))

# 2、*：左侧字符重复0次或无穷次，性格贪婪
# print(re.findall('ab*','a ab abb abbbbbbbb bbbbbbbb'))
#                                                ab*
#['a','ab','abb','abbbbbbbb']

# 3、+：左侧字符重复1次或无穷次，性格贪婪
# print(re.findall('ab+','a ab abb abbbbbbbb bbbbbbbb'))
#                         ab+

# 4、？：左侧字符重复0次或1次，性格贪婪
# print(re.findall('ab?','a ab abb abbbbbbbb bbbbbbbb'))
#                                                ab?
# ['a','ab','ab','ab']

# 5、{n,m}：左侧字符重复n次到m次，性格贪婪
# {0,} => *
# {1,} => +
# {0,1} => ?
# {n}单独一个n代表只出现n次，多一次不行少一次也不行

# print(re.findall('ab{2,5}','a ab abb abbb abbbb abbbbbbbb bbbbbbbb'))
#                                                           ab{2,5}
# ['abb','abbb','abbbb','abbbbb]

# print(re.findall('\d+\.?\d*',"asdfasdf123as1111111.123dfa12adsf1asdf3"))
#                                                                   \d+\.?\d*                                      \d+\.?\d+


# []匹配指定字符一个
# print(re.findall('a\db','a1111111b a3b a4b a9b aXb a b a\nb',re.DOTALL))
# print(re.findall('a[501234]b','a1111111b a3b a4b a9b aXb a b a\nb',re.DOTALL))
# print(re.findall('a[0-5]b','a1111111b a3b a1b a0b a4b a9b aXb a b a\nb',re.DOTALL))
# print(re.findall('a[0-9a-zA-Z]b','a1111111b axb a3b a1b a0b a4b a9b aXb a b a\nb',re.DOTALL))
#
# print(re.findall('a[^0-9a-zA-Z]b','a1111111b axb a3b a1b a0b a4b a9b aXb a b a\nb',re.DOTALL))
# print(re.findall('a-b','a-b aXb a b a\nb',re.DOTALL))
print(re.findall('a[-0-9\n]b','a-b a0b a1b a8b aXb a b a\nb',re.DOTALL))







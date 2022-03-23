# l=[111,222,333]
# l2=l # 把l的内存地址给l2
#
#
# l[0]='balabla'
# print(l)
#
# print(l2)
#
# l2[1]=4444444444444
# print(l2)
# print(l)
#
#
# del l2

# 格式化输出
# print('my name is %s age is %s' %('egon',18))
# print('成功的概率 %s%% ' % (97,))

# """
# name:{}
# age:{}
# sex:{}
# """.format('egon',18,'male')

# """
# name:{x}
# age:{y}
# sex:{z}
# """.format(z='male',x='egon',y=18)

# format新增(了解)：
# print('{x}=============='.format(x='开始执行')) # 开始执行******
# print('{x:=<10}'.format(x='开始执行')) # 开始执行******
# print('{x:=>10}'.format(x='开始执行')) # 开始执行******
# print('{x:=^10}'.format(x='开始执行')) # 开始执行******

# 四舍五入
# print('{salary:.3f}'.format(salary=1232132.12351))  #精确到小数点后3位，四舍五入，结果为：1232132.124


# x='egon'
# y=18
# res=f'name:{x} age {y}'
# print(res)

#
# x='egon'
# y=18
# res=f'name:{{{x}}} age {y}'
# print(res)

# 了解f的新用法：{}内的字符串可以被当做表达式运行
# res=f'{10+3}'
# print(res)

# f'{print("aaaa")}'


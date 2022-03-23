# 1、接收用户的输入
# 在Python3：input会将用户输入的所有内容都存成字符串类型
# username = input("请输入您的账号：")  # "egon"
# print(username, type(username))

# age = input("请输入的你的年龄： ")  # age="18"
# print(age, type(age))
# age=int(age) # int只能将纯数字的字符串转成整型
# print(age > 16)

# int("12345")
# int("1234.5")
# int("1234abc5")


# 在python2中：
# raw_input():用法与python3的input一模一样
# input(): 要求用户必须输入一个明确的数据类型，输入的是什么类型，就存成什么类型
# >>> age=input(">>>>>>>>>>>>>>>>>>>>>: ")
# >>>>>>>>>>>>>>>>>>>>>: 18
# >>> age,type(age)
# (18, <type 'int'>)
# >>>
# >>> x=input(">>>>>>>>>>>>>>>>>>>>>: ")
# >>>>>>>>>>>>>>>>>>>>>: 1.3
# >>> x,type(x)
# (1.3, <type 'float'>)
# >>>
# >>> x=input(">>>>>>>>>>>>>>>>>>>>>: ")
# >>>>>>>>>>>>>>>>>>>>>: [1,2,3]
# >>> x,type(x)
# ([1, 2, 3], <type 'list'>)
# >>>


# 2。字符串的格式化输出
# 2.1 %
# 值按照位置与%s一一对应，少一个不行，多一个也不行
# res="my name is %s my age is %s" %('egon',"18")
# res="my name is %s my age is %s" %("18",'egon')
# res="my name is %s" %"egon"
# print(res)

# 以字典的形式传值，打破位置的限制
# res="我的名字是 %(name)s 我的年龄是 %(age)s" %{"age":"18","name":'egon'}
# print(res)

# %s可以接收任意类型
# print('my age is %s' %18)
# print('my age is %s' %[1,23])
# print('my age is %s' %{'a':333})
# print('my age is %d' %18) # %d只能接收int
# print('my age is %d' %"18")

# 2.2 str.format:兼容性好
# 按照位置传值
# res='我的名字是 {} 我的年龄是 {}'.format('egon',18)
# print(res)

# res='我的名字是 {0}{0}{0} 我的年龄是 {1}{1}'.format('egon',18)
# print(res)

# 打破位置的限制，按照key=value传值
# res="我的名字是 {name} 我的年龄是 {age}".format(age=18,name='egon')
# print(res)

# 了解知识
"""
2.4 填充与格式化
# 先取到值,然后在冒号后设定填充格式：[填充字符][对齐方式][宽度]
# *<10：左对齐，总共10个字符，不够的用*号填充
print('{0:*<10}'.format('开始执行')) # 开始执行******

# *>10：右对齐，总共10个字符，不够的用*号填充
print('{0:*>10}'.format('开始执行')) # ******开始执行

# *^10：居中显示，总共10个字符，不够的用*号填充
print('{0:*^10}'.format('开始执行')) # ***开始执行***
2.5 精度与进制

print('{salary:.3f}'.format(salary=1232132.12351))  #精确到小数点后3位，四舍五入，结果为：1232132.124
print('{0:b}'.format(123))  # 转成二进制，结果为：1111011
print('{0:o}'.format(9))  # 转成八进制，结果为：11
print('{0:x}'.format(15))  # 转成十六进制，结果为：f
print('{0:,}'.format(99812939393931))  # 千分位格式化，结果为：99,812,939,393,931

"""

# 2.3 f:python3.5以后才推出
x = input('your name: ')
y = input('your age: ')
res = f'我的名字是{x} 我的年龄是{y}'
print(res)

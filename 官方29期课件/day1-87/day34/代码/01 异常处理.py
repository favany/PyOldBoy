"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""
# 1、什么是异常
# 异常是程序发生错误的信号，程序一旦出错就会抛出异常，程序的运行随即终止
#
# print('start....')
# [1,2,3][1000]
# print('stop...')
# 1.1 异常处理的三个特征
# 异常的追踪信息
# 异常的类型
# 异常的内容

# 2、为何处理异常
# 为了增强程序的健壮性，即便是程序运行过程中出错了，也不要终止程序
# 而是捕捉异常并处理：将出错信息记录到日志内

# 3、如何处理异常？
# 3.1 语法上的错误SyntaxError,
# 处理方式一：必须在程序运行前就改正
# if 1>3
#     print("run...")

# 3.2 逻辑上的错误
# print(x)

# l=['a','b']
# l[2]


# 1/0

# int('abc')

# dic={'name':'egon'}
# dic['age']

# class Foo:
#     pass

# Foo.x


# 3.2 针对逻辑上的异常又分成两种处理方式
# 3.2.1 错误发生的条件是可以预知的，使用if判断来解决
# age=input('>>: ').strip() # 输入的只要不是数字就会出错
# if age.isdigit():
#     age=int(age)
#     if age > 18:
#         print('猜大了')
#     elif age < 18:
#         print('猜大了')
#     else:
#         print('猜对了')
# else:
#     print('必须输入数字')

# 3.2.2 错误发生的条件是无法预知的
# print('start...')
# try:
#     # 有可能会抛出异常的代码
#     子代码1
#     子代码2
#     子代码3
# except 异常类型1 as e:
#     pass
# except 异常类型2 as e:
#     pass
# ...
# else:
#     如果被检测的子代码块没有异常发生，则会执行else的子代码
# finally:
#     无论被检测的子代码块有无异常发生，都会执行finally的子代码
#
# print('end...')


# # 用法一：
# print('start...')
#
# try:
#     print('1111111111')
#     l=['aaa','bbbb']
#     l[3] # 抛出异常IndexError,该行代码同级别的后续代码不会运行
#     print('2222222222')
#     xxx
#     print('33333333')
#     dic={'a':1}
#     dic['a']
# except IndexError as e:
#     print('异常的信息: ',e)
#
# print('end....')


# # 用法二：
# print('start...')
#
# try:
#     print('1111111111')
#     l=['aaa','bbbb']
#     # l[3] # 抛出异常IndexError,该行代码同级别的后续代码不会运行
#     print('2222222222')
#     xxx
#     print('33333333')
#     dic={'a':1}
#     dic['a']
# except IndexError as e:
#     print('异常的信息: ',e)
# except NameError as e:
#     print('异常的信息: ',e)
#
# print('end....')


# # 用法三：
# print('start...')
#
# try:
#     print('1111111111')
#     l = ['aaa', 'bbbb']
#     l[3] # 抛出异常IndexError,该行代码同级别的后续代码不会运行
#     print('2222222222')
#     xxx
#     print('33333333')
#     dic = {'a': 1}
#     dic['aaa']
# # except (IndexError, NameError) as e:
# #     print('异常的信息: ', e)
# # except KeyError as e:
# #     print('字典的key不存在: ', e)
# except Exception as e:  # 万能异常
#     print('所有异常都可以匹配的到')
# print('end....')


# # 用法四：else不能单独与try配合使用，必须要搭配except
# print('start...')
#
# try:
#     print('1111111111')
#     print('2222222222')
#     print('33333333')
# except Exception as e:  # 万能异常
#     print('所有异常都可以匹配的到')
# else:
#     print('====>')
#
# print('end....')

# 用法五：finally可以单独与try配合使用
print('start...')

try:
    print('1111111111')
    l = ['aaa', 'bbbb']
    l[3] # 抛出异常IndexError,该行代码同级别的后续代码不会运行
    print('2222222222')
    xxx
    print('33333333')
    dic = {'a': 1}
    dic['aaa']
finally: # 不处理异常，无论是否发生异常都会执行finally的子代码
    print('====》》》》》应该把被检测代码中回收系统资源的代码放到这里')

print('end....')

























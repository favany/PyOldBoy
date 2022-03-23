# 1、循环的语法与基本使用
'''
print(1)
while 条件:
     代码1
     代码2
     代码3
print(3)
'''

# count=0
# while count < 5: # 5 < 5
#     print(count) # 0,1,2,3,4
#     count+=1 # 5
#
# print('顶级代码----->')


# 2、死循环与效率问题
# count=0
# while count < 5: # 5 < 5
#     print(count) # 0,1,2,3,4

# while True:
#     name=input('your name >>>> ')
#     print(name)

# 纯计算无io的死讯会导致致命的效率问题
# while True:
#     1+1

# while 1:
#     print('xxxx')

# 3、循环的应用
username = 'egon'
password = '123'

# 两个问题：
# 1、重复代码
# 2、输对了应该不用再重复
# while True:
#     inp_name=input('请输入您的账号：')
#     inp_pwd=input('请输入您的密码：')
#
#     if inp_name  == username and inp_pwd == password:
#         print('登录成功')
#     else:
#         print('账号名或密码错误')


# 4、退出循环的两种方式
# 方式一：将条件改为False,等到下次循环判断条件时才会生效
# tag=True
# while tag:
#     inp_name=input('请输入您的账号：')
#     inp_pwd=input('请输入您的密码：')
#
#     if inp_name  == username and inp_pwd == password:
#         print('登录成功')
#         tag = False # 之后的代码还会运行，下次循环判断条件时才生效
#     else:
#         print('账号名或密码错误')
#
#     # print('====end====')

# 方式二：break，只要运行到break就会立刻终止本层循环
# while True:
#     inp_name=input('请输入您的账号：')
#     inp_pwd=input('请输入您的密码：')
#
#     if inp_name  == username and inp_pwd == password:
#         print('登录成功')
#         break # 立刻终止本层循环
#     else:
#         print('账号名或密码错误')
#
#     # print('====end====')


# 7、while循环嵌套与结束
'''
tag=True
while tag:
    while tag:
        while tag:
            tag=False
    

# 每一层都必须配一个break
while True:
    while True:
        while True:
            break
        break
    break
'''
## break的方式
# while True:
#     inp_name=input('请输入您的账号：')
#     inp_pwd=input('请输入您的密码：')
#
#     if inp_name  == username and inp_pwd == password:
#         print('登录成功')
#         while True:
#             cmd=input("输入命令>: ")
#             if cmd == 'q':
#                 break
#             print('命令{x}正在运行'.format(x=cmd))
#         break # 立刻终止本层循环
#     else:
#         print('账号名或密码错误')
#
#     # print('====end====')

# # 改变条件的方式
# tag=True
# while tag:
#     inp_name=input('请输入您的账号：')
#     inp_pwd=input('请输入您的密码：')
#
#     if inp_name  == username and inp_pwd == password:
#         print('登录成功')
#         while tag:
#             cmd=input("输入命令>: ")
#             if cmd == 'q':
#                 tag=False
#             else:
#                 print('命令{x}正在运行'.format(x=cmd))
#     else:
#         print('账号名或密码错误')


# 8、while +continue：结束本次循环，直接进入下一次
# 强调：在continue之后添加同级代码毫无意义，因为永远无法运行
# count=0
# while count < 6:
#     if count == 4:
#         count+=1
#         continue
#         # count+=1 # 错误
#     print(count)
#     count+=1

# 9、while +else：针对break
# count=0
# while count < 6:
#     if count == 4:
#         count+=1
#         continue
#     print(count)
#     count+=1
# else:
#     print('else包含的代码会在while循环结束后，并且while循环是在没有被break打断的情况下正常结束的，才不会运行')

# count=0
# while count < 6:
#     if count == 4:
#         break
#     print(count)
#     count+=1
# else:
#     print('======>')


# 应用案列：
# 版本1：
# count=0
# tag=True
# while tag:
#     if count == 3:
#         print('输错三次退出')
#         break
#     inp_name=input('请输入您的账号：')
#     inp_pwd=input('请输入您的密码：')
#
#     if inp_name  == username and inp_pwd == password:
#         print('登录成功')
#         while tag:
#             cmd=input("输入命令>: ")
#             if cmd == 'q':
#                 tag=False
#             else:
#                 print('命令{x}正在运行'.format(x=cmd))
#     else:
#         print('账号名或密码错误')
#         count+=1

# 版本2：优化
count=0
while count < 3:
    inp_name=input('请输入您的账号：')
    inp_pwd=input('请输入您的密码：')

    if inp_name  == username and inp_pwd == password:
        print('登录成功')
        while True:
            cmd=input("输入命令>: ")
            if cmd == 'q': # 整个程序结束，退出所有while循环
                break
            else:
                print('命令{x}正在运行'.format(x=cmd))
        break
    else:
        print('账号名或密码错误')
        count+=1
else:
    print('输错3次，退出')

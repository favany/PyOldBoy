'''
1、什么是for循环
    循环就是重复做某件事，for循环是python提供第二种循环机制

2、为何要有for循环
    理论上for循环能做的事情，while循环都可以做
    之所以要有for循环，是因为for循环在循环取值（遍历取值）比while循环更简洁

3、如何用for循环
语法：
for 变量名 in 可迭代对象:# 可迭代对象可以是：列表、字典、字符串、元组、集合
    代码1
    代码2
    代码3
    ...
'''
# 一：for基本使用之循环取值
# 案例1：列表循环取值
# 简单版
# l = ['alex_dsb', 'lxx_dsb', 'egon_nb']
# for x in l:  # x='lxx_dsb'
#     print(x)

# 复杂版：
# l = ['alex_dsb', 'lxx_dsb', 'egon_nb']
# i=0
# while i < 3:
#     print(l[i])
#     i+=1


# 案例2：字典循环取值
# 简单版
# dic={'k1':111,'k2':2222,'k3':333}
# for k in dic:
#     print(k,dic[k])

# 复杂版：while循环可以遍历字典，太麻烦了

# 案例3：字符串循环取值
# 简单版
# msg="you can you up,no can no bb"
# for x in msg:
#     print(x)

# 复杂版：while循环可以遍历字典，太麻烦了


# 二：总结for循环与while循环的异同
# 1、相同之处：都是循环，for循环可以干的事，while循环也可以干
# 2、不同之处：
#           while循环称之为条件循环，循环次数取决于条件何时变为假
#           for循环称之为"取值循环"，循环次数取决in后包含的值的个数
# for x in [1,2,3]:
#     print('===>')
#     print('8888')


# 三：for循环控制循环次数：range()
# in后直接放一个数据类型来控制循环次数有局限性：
#                 当循环次数过多时，数据类型包含值的格式需要伴随着增加
# for x in 'a c':
#     inp_name=input('please input your name:   ')
#     inp_pwd=input('please input your password:   ')
#

# range功能介绍
'''
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> range(1,9) # 1...8
[1, 2, 3, 4, 5, 6, 7, 8]
>>> 
>>> range(1,9,1) # 1 2 3 4 5 6 7 8 
[1, 2, 3, 4, 5, 6, 7, 8]
>>> range(1,9,2) # 1 3 5 7 
[1, 3, 5, 7]
'''
# for i in range(30):
#     print('===>')


# for+break: 同while循环一样
# for+else：同while循环一样
# username='egon'
# password='123'
# for i in range(3):
#     inp_name = input('请输入您的账号：')
#     inp_pwd = input('请输入您的密码：')
#
#     if inp_name == username and inp_pwd == password:
#         print('登录成功')
#         break
# else:
#     print('输错账号密码次数过多')


# 四：range补充知识（了解）
# 1、for搭配range，可以按照索引取值，但是麻烦，所以不推荐
# l=['aaa','bbb','ccc'] # len(l)
# for i in range(len(l)):
#     print(i,l[i])
#
# for x in l:
#     print(l)
# 2、range()在python3里得到的是一只"会下蛋的老母鸡"


# 五：for+continue
# for i in range(6):  # 0 1 2 3 4 5
#     if i == 4:
#         continue
#     print(i)

# 六：for循环嵌套:外层循环循环一次，内层循环需要完整的循环完毕
# for i in range(3):
#     print('外层循环-->', i)
#     for j in range(5):
#         print('内层-->', j)

# 补充：终止for循环只有break一种方案

# print('hello %s' % 'egon')
# 1、print之逗号的使用
# print('hello','world','egon')
# 2、换行符
# print('hello\n')
# print('world')
# 3、print值end参数的使用
# print('hello\n',end='')
# print('word')
print('hello',end='*')
print('world',end='*')
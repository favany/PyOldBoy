# 1、算数运算符
# print(10 + 3.1)
# print(10 + 3)
# print(10 / 3)  # 结果带小数
# print(10 // 3)  # 只保留整数部分
# print(10 % 3) # 取模、取余数
# print(10 ** 3) # 取模、取余数

# 2、比较运算符: >、>=、<、<=、==、!=
# print(10 > 3)
# print(10 == 10)
#
# print(10 >= 10)
# print(10 >= 3)

# name=input('your name: ')
# print(name == 'egon')


# 3、赋值运算符
# 3.1 =：变量的赋值
# 3.2 增量赋值：
# age = 18
# # age += 1  # age=age + 1
# # print(age)
#
# age*=3
# age/=3
# age%=3
# age**=3 # age=age**3

# 3.3 链式赋值
# x=10
# y=x
# z=y
# z = y = x = 10 # 链式赋值
# print(x, y, z)
# print(id(x), id(y), id(z))

# 3.4 交叉赋值
m=10
n=20
# print(m,n)
# 交换值
# temp=m
# m=n
# n=temp
# print(m,n)

# m,n=n,m # 交叉赋值
# print(m,n)

# 3.5 解压赋值
salaries=[111,222,333,444,555]
# 把五个月的工资取出来分别赋值给不同的变量名
# mon0=salaries[0]
# mon1=salaries[1]
# mon2=salaries[2]
# mon3=salaries[3]
# mon4=salaries[4]

# 解压赋值
# mon0,mon1,mon2,mon3,mon4=salaries
# print(mon0)
# print(mon1)
# print(mon2)
# print(mon3)
# print(mon4)

# mon0,mon1,mon2,mon3=salaries # 对应的变量名少一个不行
# mon0,mon1,mon2,mon3,mon4,mon5=salaries # 对应的变量名多一个也不行

# 引入*，可以帮助我们取两头的值，无法取中间的值
# 取前三个值
# x,y,z,*_=salaries=[111,222,333,444,555] # *会将没有对应关系的值存成列表然后赋值给紧跟其后的那个变量名，此处为_
# print(x,y,z)
# print(_)

# 取后三个值
# *_,x,y,z=salaries=[111,222,333,444,555]
# print(x,y,z)

# x,*_,y,z=salaries=[111,222,333,444,555]
# print(x,y,z)

# salaries=[111,222,333,444,555]
# _,*middle,_=salaries
# print(middle)

# 解压字典默认解压出来的是字典的key
x,y,z=dic={'a':1,'b':2,'c':3}
print(x,y,z)


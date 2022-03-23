# 1、可变不可变类型

# 可变类型：值改变，id不变，证明改的是原值，证明原值是可以被改变的
# 不可变类型：值改变，id也变了，证明是产生新的值，压根没有改变原值，证明原值是不可以被修改的

# 2、验证
# 2.1 int是不可变类型
# x=10
# print(id(x))
# x=11 # 产生新值
# print(id(x))

# 2.2 float是不可变类型
# x=3.1
# print(id(x))
# x=3.2
# print(id(x))

# 2.3 str是不可变类型
# x="abc"
# print(id(x))
# x='gggg'
# print(id(x))

# 小结：int、float、str都被设计成了不可分割的整体，不能够被改变


# 2.4 list是可变类型
# l=['aaa','bbb','ccc']
# print(id(l))
# l[0]='AAA'
# print(l)
# print(id(l))

# 2.5 dict
# dic={'k1':111,'k2':222}
# print(id(dic))
# dic['k1']=3333333333
# # print(dic)
# print(id(dic))


#2.6 bool不可变


# 关于字典补充：
# 定义：{}内用逗号分隔开多key:value,
#           其中value可以是任意类型
#           但是key必须是不可变类型

# dic={
#     'k1':111,
#     'k2':3.1,
#     'k3':[333,],
#     'k4':{'name':'egon'}
# }
#
# dic={
#     2222:111,
#     3.3:3.1,
#     'k3':[333,],
#     'k4':{'name':'egon'}
# }
# print(dic[3.3])

# dic={[1,2,3]:33333333}
# dic={{'a':1}:33333333}







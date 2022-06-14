# @File      : 01 集合
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/6/6 9:30 AM
# @Info      :

# 集合
# 1、作用
# 集合有两大作用：关系运算和去重

# 集合的作用之关系运算
# 列表
friends1 = ["zero", "kevin", "jason", "egon"]
friends2 = ["Jy", "ricky", "jason", "egon"]
# 找到共同好友
l = []
for x in friends1:
    if x in friends2:
        l.append(x)
print(l)

# 2. 定义
# 在 {} 内用逗号分隔开多个元素，必须满足以下三个条件：
# 集合内元素必须为不可变类型
# 集合内元素无序
# 集合内元素没有重复

s = {1, 2}  # s = set({1, 2})

# s = {1, [1, 2]}  # ❌ 集合内的元素必须为不可变类型
s = {1, 'a', 'b', 4, 7}  # 集合内元素无序
# s = {1, 1, 1, 1}  # ❌ 集合内元素没有重复

# 了解
s = {}  # 默认是空字典
print(s, type(s))

# 定义空集合
s = set()
print(s, type(s))

# 3. 类型转换
res1 = set({1, 2, 3})  # {1, 2, 3}
res2 = set("hellollll")  # {'l', 'o', 'h', 'e'}
res3 = set([1, 1, 1, 1])  # {1}
print(res1, res2, res3)

# 4. 内置方法
friends1 = {"zero", "kevin", "jason", "egon"}
friends2 = {"Jy", "ricky", "jason", "egon"}

# 4.1 取共同好友 -- 交集
common_friends = friends1 & friends2
print("common friends", common_friends)
# print(friends1.intersection(friends2))

# 4.2 取全部好友 -- 并集/合集
total_friends = friends1 | friends2
print("total friends", total_friends)
# print(friends1.union(friends2))

# 4.3
# 取 friends1 独有的好友
diff_friend1 = friends1 - friends2
print("diff friend1", diff_friend1)
# print(friends1.difference(friends2))

# 取 friends2 独有的好友
diff_friend2 = friends2 - friends1
print("diff friend2", diff_friend2)
# print(diff_friend2.difference(friends1))

# 4.4 对称差集：取 friends1 和 friends2 各自的独有好友
# (friends1 - friends2) | (friends2 - friends1)

diff_friend = friends1 ^ friends2
print("diff friend", diff_friend)
print(friends1.symmetric_difference(friends2))

# 4.5 父子集：包含的关系
s1 = {1, 2, 3}
s2 = {1, 2, 4}
s3 = {1}
s4 = {1, 2, 3}
print(s1 > s2)  # False
print(s1 > s3)  # True

print(s1.issuperset(s3))  # s1 > s3
print(s3.issubset(s1))  # s3 < s1

print(s1 == s4 )  # s1 与 s4 互为父子







# @File      : 01 集合 - 去重
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/6/6 11:35 AM
# @Info      :

# 集合 的作用之去重
# 1、只能针对不可变类型去重
# print(set([1, 1, 1, 1, 2]))

# 2、无法保证原来的顺序
# l = [1, 'a', 'b', 1, 1, 2]
# l = list(set(l))
# print(l)

people_list = [
    {'name': 'lili', 'age': 18, 'sex': 'male'},
    {'name': 'jack', 'age': 18, 'sex': 'male'},
    {'name': 'tom', 'age': 18, 'sex': 'female'},
]
new_people_list = []
for dic in people_list:
    if dic not in new_people_list:
        new_people_list.append(dic)
print(new_people_list)

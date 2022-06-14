# @File      : 01 集合 - 其他操作
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/6/6 3:18 PM
# @Info      :

# 其他操作
# 1. 长度

s = {'a', 'b', 'c'}
print(len(s))

# 2. 成员运算
print('c' in s)

# 3. 循环
for item in s:
    print(item)

# 4.删除元素（掌握）
# 如果括号内是集合中的元素，则删除该元素。删除不存在的元素，则不操作。
s.discard("a")
print(s)

# s.remove() 删除不存在的元素会报错

# 5. 更新原集合（掌握） 原集合存在的话不操作，不存在的话就把元素加入
s.update({"c", "d"})
print("after update", s)

# 6. 随机取出一个元素（掌握）
res = s.pop()
print("取出来的元素", res, "取出后的集合", s)

# 7. 判断集合是否完全没有交集
re = s.isdisjoint({3, 4, 5, 6})
print(re)

# 8. 从这个集合中删除另一个集合的所有元素
s.difference_update({"a", "c"})
print(s)
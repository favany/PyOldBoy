"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""

# 算法：是高效解决问题的办法
# 算法之二分法

# 需求：有一个按照从小到大顺序排列的数字列表
#      需要从该数字列表中找到我们想要的那个一个数字
#      如何做更高效？？？


nums=[-3,4,7,10,13,21,43,77,89]
find_num=10

nums=[-3,4,13,10,-2,7,89]
nums.sort()
print(nums)

# 方案一：整体遍历效率太低
# for num in nums:
#     if num == find_num:
#         print('find it')
#         break

# 方案二：二分法
# def binary_search(find_num,列表):
#     mid_val=找列表中间的值
#     if find_num > mid_val:
#         # 接下来的查找应该是在列表的右半部分
#         列表=列表切片右半部分
#         binary_search(find_num,列表)
#     elif find_num < mid_val:
#         # 接下来的查找应该是在列表的左半部分
#         列表=列表切片左半部分
#         binary_search(find_num,列表)
#     else:
#         print('find it')

# nums=[-3,4,7,10,13,21,43,77,89]
# find_num=8
# def binary_search(find_num,l):
#     print(l)
#     if len(l) == 0:
#         print('找的值不存在')
#         return
#     mid_index=len(l) // 2
#
#     if find_num > l[mid_index]:
#         # 接下来的查找应该是在列表的右半部分
#         l=l[mid_index+1:]
#         binary_search(find_num,l)
#     elif find_num < l[mid_index]:
#         # 接下来的查找应该是在列表的左半部分
#         l=l[:mid_index]
#         binary_search(find_num,l)
#     else:
#         print('find it')
#
# binary_search(find_num,nums)












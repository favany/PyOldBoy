# @File      : 01 二分法
# @Author    : 刘俊 mophia
# @Time      : 2022/6/19 5:11 PM

"""
算法：高效的解决问题的方法

算法之二分法

需求：有一个按照从小到大顺序排列的数字列表.需要从改数字列表中找到我们想要的哪那个数字，如何做更高效。
"""


nums = [-3, 4, 7, 10, 11, 13, 43, 77, 89]
nums.sort()
find_num = 13

# 方案一：整体遍历效率太低
# for num in nums:
#     if num == find_num:
#         print("find it")
#         break

# 方案二：二分法


def binary_search(find_num, l):
    print(l)
    if len(l) == 0:
        print("找的值不存在")
        return
    mid_index = len(l) // 2

    if find_num > l[mid_index]:
        # 接下来的查找 应该是在列表的右半部分
        l = l[mid_index + 1:]
        binary_search(find_num, l)

    elif find_num < l[mid_index]:
        # 接下来的查找 应该是在列表的左半部分
        l = l[:mid_index]
        binary_search(find_num, l)

    else:
        print("find it")


binary_search(find_num, nums)


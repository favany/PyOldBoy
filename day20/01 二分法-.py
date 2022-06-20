



"""
算法：高效解决问题的办法

二分法
需求：有一个按照从小到大排列的数字列表 需要从该数字列表中找到想要的数字 如何做更高效？
"""

nums = [-3, 4, 7, 10, 11, 13, 43, 77, 89]
nums.sort()
find_num = 8

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


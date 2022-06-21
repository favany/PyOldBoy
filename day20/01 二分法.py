# @File      : 01 二分法
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/6/19 5:11 PM
# @Info      :

"""
算法：高效的解决问题的方法

算法之二分法

需求：有一个按照从小到大顺序排列的数字列表.需要从改数字列表中找到我们想要的哪那个数字，如何做更高效。
"""

nums = [3, 4, 7, 10, 13, 21, 43, 77, 89]
find_num = 13

# 方案一：整体遍历，效率太低
for num in nums:
    if num == find_num:
        print("find it")
        break

# 方案二：二分法


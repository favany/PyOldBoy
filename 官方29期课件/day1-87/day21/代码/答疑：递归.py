"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""

nums=[-3,4,7,10,13,21,43,77,89]
find_num=8
def binary_search(find_num,l):
    print(l)
    if len(l) == 0:
        print('找的值不存在')
        return False
    mid_index=len(l) // 2

    if find_num > l[mid_index]:
        # 接下来的查找应该是在列表的右半部分
        l=l[mid_index+1:]
        return binary_search(find_num,l)
    elif find_num < l[mid_index]:
        # 接下来的查找应该是在列表的左半部分
        l=l[:mid_index]
        return binary_search(find_num,l)
    else:
        print('find it')
        return True

res=binary_search(7,nums)
print(res)



# def salary(n): # n = 3
#     if n==1:
#         return 5000
#     res=salary(n-1)+1000 # 6000 + 1000
#
#     return res
#
# res=salary(4) # salary(4)=>salary(3)+1000
#
#
#
# salary(4)=>salary(3) + 1000=>salary(2)+1000=>salary(1) + 1000
# salary(4)=>7000 + 1000=>6000+1000<=5000 + 1000
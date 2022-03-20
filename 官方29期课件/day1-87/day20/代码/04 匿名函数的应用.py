"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""

salaries={
    'siry':3000,
    'tom':7000,
    'lili':10000,
    'jack':2000
}
# 需求1：找出薪资最高的那个人=》lili
# res=max([3,200,11,300,399])
# print(res)

# res=max(salaries)
# print(res)


salaries={
    'siry':3000,
    'tom':7000,
    'lili':10000,
    'jack':2000
}
# 迭代出的内容    比较的值
# 'siry'         3000
# 'tom'          7000
# 'lili'         10000
# 'jack'         2000

# def func(k):
#     return salaries[k]

# ========================max的应用
# res=max(salaries,key=func) # 返回值=func('siry')
# print(res)

# res=max(salaries,key=lambda k:salaries[k])
# print(res)

# ========================min的应用
# res=min(salaries,key=lambda k:salaries[k])
# print(res)


# ========================sorted排序
# salaries={
#     'siry':3000,
#     'tom':7000,
#     'lili':10000,
#     'jack':2000
# }
res=sorted(salaries,key=lambda k:salaries[k],reverse=True)
# print(res)

# ========================map的应用(了解)
# l=['alex','lxx','wxx','薛贤妻']
# new_l=(name+'_dsb' for name in l)
# print(new_l)

# res=map(lambda name:name+'_dsb',l)
# print(res) # 生成器
# ========================filter的应用（了解）
# l=['alex_sb','lxx_sb','wxx','薛贤妻']
# res=(name for name in l if name.endswith('sb'))
# print(res)

# res=filter(lambda name:name.endswith('sb'),l)
# print(res)

# ========================reduce的应用(了解)
from functools import reduce
res=reduce(lambda x,y:x+y,[1,2,3],10) # 16
print(res)

res=reduce(lambda x,y:x+y,['a','b','c']) # 'a','b'
print(res)



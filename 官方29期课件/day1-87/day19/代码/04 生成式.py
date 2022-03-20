"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""

# 1、列表生成式
l = ['alex_dsb', 'lxx_dsb', 'wxx_dsb', "xxq_dsb", 'egon']
# new_l=[]
# for name in l:
#     if name.endswith('dsb'):
#         new_l.append(name)


# new_l=[name for name in l if name.endswith('dsb')]
# new_l=[name for name in l]

# print(new_l)

# 把所有小写字母全变成大写
# new_l=[name.upper() for name in l]
# print(new_l)

# 把所有的名字去掉后缀_dsb
# new_l=[name.replace('_dsb','') for name in l]
# print(new_l)

# 2、字典生成式
# keys=['name','age','gender']
# dic={key:None for key in keys}
# print(dic)

# items=[('name','egon'),('age',18),('gender','male')]
# res={k:v for k,v in items if k != 'gender'}
# print(res)

# 3、集合生成式
# keys=['name','age','gender']
# set1={key for key in keys}
# print(set1,type(set1))


# 4、生成器表达式
# g=(i for i in range(10) if i > 3)
# ！！！！！！！！！！！强调！！！！！！！！！！！！！！！
# 此刻g内部一个值也没有

# print(g,type(g))

# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


with open('笔记.txt', mode='rt', encoding='utf-8') as f:
    # 方式一：
    # res=0
    # for line in f:
    #     res+=len(line)
    # print(res)

    # 方式二：
    # res=sum([len(line) for line in f])
    # print(res)

    # 方式三 ：效率最高
    # res = sum((len(line) for line in f))
    # 上述可以简写为如下形式
    res = sum(len(line) for line in f)
    print(res)
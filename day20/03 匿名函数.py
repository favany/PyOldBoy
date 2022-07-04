# @File      : 03 匿名函数
# @Author    : 刘俊 mophia
# @Time      : 2022/6/19 6:01 PM
# @Info      :

"""
1. 有名函数
func = 函数的内存地址
"""
def func(x, y):
    return x+y


"""
2. 匿名函数
"""
lambda x,y: x + y


"""
3. 调用匿名函数
方式一：
"""
re = (lambda x, y: x + y)(1,2)
print(re)

"""
方式二：
"""
func = lambda x, y : x + y
re = func(1, 2)
print(re)

"""
4. 匿名用于临时调用一次的场景：更多的是将匿名函数与其他函数配合使用.
"""


salaries = {
    "siry": 3000,
    "tom": 7000,
    "lili": 10000,
    "jack": 2000
}

# 需求1：找出薪资最高的那个人 => lili
re = max(salaries)  # 单纯根据 key 的ASCII码排序
print(re)

re = max(salaries, key=lambda k: salaries[k])  # 根据 value 排序，然后返回 key 值
print(re)

# map 的应用


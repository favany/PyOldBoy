# @File      : 04 匿名函数的应用
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/6/19 10:29 PM
# @Info      :

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

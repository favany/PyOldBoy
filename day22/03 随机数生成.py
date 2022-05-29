# @File      : 03 随机数生成
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/5/28 5:00 PM
# @Info      :

import random

# 生成 0-1 之间的随机数
ran = random.random()
print(ran)

# 生成随机整数
# 生成 [1, 10] 大于等于 1 , 小于等于 10 的整数
ran2 = random.randint(1, 10)
# 生成 [1, 10) 大于等于 1 , 小于 10 的整数
ran3 = random.randrange(1, 10)
print(ran2, ran3)

# random.choice(list) 多选一
ran4 = random.choice([1, '23', [4, 5]])
print(ran4)

# random.sample(list, n) 多选 n
ran5 = random.sample([1, '23', [4, 5]], 2)
print(ran5)

# random.uniform(m, n) 随机生成 m 到 n 之间的小数
ran6 = random.uniform(1, 10)
print(ran6)

# random.sh
ran7 = [1, 2, 3, 4, 5]
random.shuffle(ran7)
print(ran7)


# 应用：随机生成验证码 x12abc
def make_random_code(count): # count是位数
    ran8 = ""
    for i in range(count):
        # 随机字符 = random.choice([从26小写字母随机抽取一个，从10个数字中随机抽取一个])
        number = str(random.randint(0, 9))
        # ASCII -> 字符 chr()， 字符 -> ASCII ord()
        string = chr(random.randint(97, 122))
        ran8 += random.choice([number, string])
    return ran8


print(make_random_code(6))







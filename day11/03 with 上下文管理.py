# @File      : 02 with 上下文管理
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/6/9 5:13 PM
# @Info      : with 上下文管理


# with 上下文管理

# \ 代表上下两行的内容是同一行

with open('path/a.txt', mode='rt') as f1, \
        open('path/b.txt', mode='rt') as f2:
    res1 = f1.read()
    res2 = f2.read()
    print(res1, res2)

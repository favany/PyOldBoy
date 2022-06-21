# @File      : 04 函数传参的两种方式
# @Author    : 刘俊 mophia
# @Email     : contact@mophia.com
# @Work Email: jun.liu@deepfinance.com
# @Time      : 2022/6/19 8:14 AM
# @Info      :

import requests


def get(url):
    response = requests.get(url)
    print(response.text)


# get("https://www.baidu.com")
# get("https://www.cnblogs.com/linhaifeng")
# get("https://www.mophia.com")


def outter(url):
    def get():
        response = requests.get(url)
        print(response.text)
    return get()


zhihu = outter("https://www.douban.com")

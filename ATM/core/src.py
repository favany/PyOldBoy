"""
@Time    : 2022/7/4 11:06
@Author  : 刘俊 jun.liu@deepfinance.com
@File    : src.py
"""


import time


def login():
    ...

def register():
    ...

def witdraw():
    print('提现功能')

def transfer():
    print('转账功能')

func_dict = {
    '0': ['退出', exit],
    '1': ['登陆', login],
    '2': ['注册', register],
    '3': ['提现', witdraw],
    '4': ['转账', transfer]
}


def run():
    while True:
        for k, v in func_dict.items():
            print(k, v[0])

        choice = input('请输入指令编号：').strip()
        func_dict[choice][1]()


def logger(msg):
    with open(r'/Users/admin/Projects/PyOldBoy/ATM/log/user.log', mode="at", encoding="utf-8")  as f:
        f.write('%s %s \n' % (time.strftime('%Y-%m-%d %H:%M:%S'), msg))
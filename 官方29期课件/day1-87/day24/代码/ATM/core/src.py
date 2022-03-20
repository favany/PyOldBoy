"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""
from lib.common import logger

def login():
    print('登录功能')
    logger('egon刚刚登录了')

def register():
    print('注册功能')
    logger('egon刚刚注册了')

def witdraw():
    print('提现功能正在运行')
    logger('egon刚刚提现了3毛钱')

def transfer():
    print('转账功能')
    logger('egon刚刚给alex转了3个亿冥币')


func_dic={
    '0':['退出',exit],
    '1':['登录',login],
    '2':['注册',register],
    '3':['提现',witdraw],
    '4':['转账',transfer],
}

def run():
    while True:
        for k in func_dic:
            print(k,func_dic[k][0])

        choice=input('请输入指令编号: ').strip()
        if choice in func_dic:
            func_dic[choice][1]()
        else:
            print('请输入输入')




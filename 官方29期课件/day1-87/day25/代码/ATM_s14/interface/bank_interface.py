'''
银行相关业务的接口
'''
from db import db_handler


# 提现接口(手续费5%)
def withdraw_interface(username, money):
    # 1) 先获取用户字典
    user_dic = db_handler.select(username)
    # 账户中的金额
    balance = int(user_dic.get('balance'))

    # 提现本金 + 手续费
    money2 = int(money) * 1.05  # ---> float

    # 判断用户金额是否足够
    if balance >= money2:
        # 2）修改用户字典中的金额
        balance -= money2

        user_dic['balance'] = balance

        # 3）再保存数据，或更新数据
        db_handler.save(user_dic)

        return True, f'用户[{username}] 提现金额[{money}$]成功，手续费为: [{money2 - float(money)}$]'

    return False, '提现金额不足，请重新输入!'


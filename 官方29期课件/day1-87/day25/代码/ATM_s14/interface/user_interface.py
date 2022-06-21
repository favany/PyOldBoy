'''
逻辑接口层
    用户接口
'''
from db import db_handler
from lib import common


# 注册接口
def register_interface(username, password, balance=15000):
    # 2）查看用户是否存在
    # 2.1) 调用 数据处理层 中的 select函数，会返回 用户字典 或 None
    user_dic = db_handler.select(username)

    # {user: user, pwd: pwd...}   or  None
    # 若用户存在，则return，告诉用户重新输入
    if user_dic:
        # return (False, '用户名已存在!')
        return False, '用户名已存在!'

    # 3）若用户不存在，则保存用户数据
    # 做密码加密
    password = common.get_pwd_md5(password)

    # 3.1) 组织用户的数据的字典信息
    user_dic = {
        'username': username,
        'password': password,
        'balance': balance,
        # 用于记录用户流水的列表
        'flow': [],
        # 用于记录用户购物车
        'shop_car': {},
        # locked：用于记录用户是否被冻结
        # False: 未冻结   True: 已被冻结
        'locked': False
    }

    # 3.2）保存数据
    db_handler.save(user_dic)

    return True, f'{username} 注册成功!'


# 登录接口
def login_interface(username, password):
    # 1) 先查看当前用户数据是否存在
    # {用户数据字典}  or  None
    user_dic = db_handler.select(username)
    # 用于判断用户否存在

    # 2) 判断用户是否存在
    if user_dic:
        # 给用户输入的密码做一次加密
        password = common.get_pwd_md5(password)
        # 3) 校验密码是否一致
        if password == user_dic.get('password'):

            return True, f'用户: [{username}] 登录成功!'

        else:
            return False, '密码错误'

    return False, '用户不存在，请重新输入！'


# 查看余额接口
def check_bal_interface(username):
    user_dic = db_handler.select(username)
    return user_dic['balance']

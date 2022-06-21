'''
用户视图层
'''
from interface import user_interface
from interface import bank_interface
from lib import common

# 全局变量，记录用户是否已登录
login_user = None


# 1、注册功能
def register():
    while True:
        # 1）让用户输入用户名与密码进行校验
        username = input('请输入用户名: ').strip()
        password = input('请输入密码: ').strip()
        re_password = input('请确认密码: ').strip()
        # 可以输入自定义的金额

        # 小的逻辑处理: 比如两次密码是否一致
        if password == re_password:
            # 2) 调用接口层的注册接口，将用户名与密码交给接口层来进行处理

            # res ---> (False, '用户名已存在!')
            # res = user_interface.register_interface(
            # flag, msg ---> (flag---> False, msg --> '用户名已存在!')

            # (True, 用户注册成功)，  (False, 注册失败)
            flag, msg = user_interface.register_interface(
                username, password
            )

            # 3) 根据flag判断用户注册是否成功，flag控制break的结束
            if flag:
                print(msg)
                break

            else:
                print(msg)


# 2、登录功能
def login():
    # 登录视图
    while True:
        # 1) 让用户输入用户名与密码
        username = input('请输入用户名: ').strip()
        password = input('请输入密码: ').strip()

        # 2）调用接口层，将数据传给登录接口
        # (True, f'用户: [{username}] 登录成功!'),
        # (return False, '密码错误'), (False, '用户不存在，请重新输入！')
        flag, msg = user_interface.login_interface(
            username, password
        )
        if flag:
            print(msg)
            global login_user
            login_user = username
            break

        else:
            print(msg)


# 3、查看余额
@common.login_auth
def check_balance():

    # 1.直接调用查看余额接口，获取用户余额
    balance = user_interface.check_bal_interface(
        login_user
    )

    print(f'用户{login_user} 账户余额为: {balance}')


# 4、提现功能
@common.login_auth
def withdraw():
    while True:
        # 1) 让用户输入提现金额
        input_money = input('请输入提现金额: ').strip()

        # 2) 判断用户输入的金额是否是数字
        if not input_money.isdigit():
            print('请重新输入')
            continue

        # 3) 用户提现金额，将提现的金额交付给接口层来处理
        flag, msg = bank_interface.withdraw_interface(
            login_user, input_money
        )

        if flag:
            print(msg)
            break
        else:
            print(msg)


# 5、还款功能
@common.login_auth
def repay():
    pass


# 6、转账功能
@common.login_auth
def transfer():
    pass


# 7、查看流水
@common.login_auth
def check_flow():
    pass


# 8、购物功能
@common.login_auth
def shopping():
    pass


# 9、查看购物车
@common.login_auth
def check_shop_car():
    pass


# 10、管理员功能
def admin():
    pass


# 创建函数功能字典
func_dic = {
    '1': register,
    '2': login,
    '3': check_balance,
    '4': withdraw,
    '5': repay,
    '6': transfer,
    '7': check_flow,
    '8': shopping,
    '9': check_shop_car,
    '10': admin,
}


# 视图层主程序
def run():
    while True:
        print('''
        ===== ATM + 购物车 =====
            1、注册功能
            2、登录功能
            3、查看余额
            4、提现功能
            5、还款功能
            6、转账功能
            7、查看流水
            8、购物功能
            9、查看购物车
            10、管理员功能
        ========= end =========
        ''')

        choice = input('请输入功能编号: ').strip()

        if choice not in func_dic:
            print('请输入正确的功能编号!')
            continue

        func_dic.get(choice)()  # func_dic.get('1')() ---> register()

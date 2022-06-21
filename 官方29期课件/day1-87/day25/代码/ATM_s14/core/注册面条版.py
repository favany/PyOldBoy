# 面条版
'''
def register():
    while True:
        # 1）让用户输入用户名与密码进行校验
        username = input('请输入用户名: ').strip()
        password = input('请输入密码: ').strip()
        re_password = input('请确认密码: ').strip()

        # 小的逻辑处理: 比如两次密码是否一致
        if password == re_password:
            import json
            import os
            from conf import settings
            user_path = os.path.join(
                settings.USER_DATA_PATH, f'{username}.json'
            )

            # 2）查看用户是否存在
            # 2.1) 若不存在，则让用户重新受保护如
            if os.path.exists(user_path):
                print('请重新输入！')

                with open(user_path, 'r', encoding='utf-8') as f:
                    user_dic = json.load(f)

                if user_dic:
                    print('用户已存在，请重新输入!')
                    continue

            # 4）若用户不存在，则保存用户数据
            # 4.1) 组织用户的数据的字典信息
            user_dic = {
                'username': username,
                'password': password,
                'balance': 15000,
                # 用于记录用户流水的列表
                'flow': [],
                # 用于记录用户购物车
                'shop_car': {},
                # locked：用于记录用户是否被冻结
                # False: 未冻结   True: 已被冻结
                'locked': False
            }

            # 存不是目的，目的是为了更方便地取数据。
            # 文件名: 用户名.json  tank.json   矮跟.json
            # 4.2）拼接用户的json文件路径
            user_path = os.path.join(
                settings.USER_DATA_PATH, f'{username}.json'
            )

            with open(user_path, 'w', encoding='utf-8') as f:
                # ensure_ascii=False让文件中的中文数据，显示更美观
                json.dump(user_dic, f, ensure_ascii=False)
'''
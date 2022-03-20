"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""


# 一：知识储备
# 由于语法糖@的限制，outter函数只能有一个参数，并且该才是只用来接收
#                                       被装饰对象的内存地址
# def outter(func):
#     # func = 函数的内存地址
#     def wrapper(*args,**kwargs):
#         res=func(*args,**kwargs)
#         return res
#     return wrapper
#
# # @outter # index=outter(index) # index=>wrapper
# @outter # outter(index)
# def index(x,y):
#     print(x,y)

# 偷梁换柱之后
# index的参数什么样子，wrapper的参数就应该什么样子
# index的返回值什么样子，wrapper的返回值就应该什么样子
# index的属性什么样子，wrapper的属性就应该什么样子==》from functools import wraps


# 山炮玩法：
# def auth(func,db_type):
#     def wrapper(*args, **kwargs):
#         name=input('your name>>>: ').strip()
#         pwd=input('your password>>>: ').strip()
#
#         if db_type == 'file':
#             print('基于文件的验证')
#             if name == 'egon' and pwd == '123':
#                 res = func(*args, **kwargs)
#                 return res
#             else:
#                 print('user or password error')
#         elif db_type == 'mysql':
#             print('基于mysql的验证')
#         elif db_type == 'ldap':
#             print('基于ldap的验证')
#         else:
#             print('不支持该db_type')
#
#     return wrapper
#
# # @auth  # 账号密码的来源是文件
# def index(x,y):
#     print('index->>%s:%s' %(x,y))
#
# # @auth # 账号密码的来源是数据库
# def home(name):
#     print('home->>%s' %name)
#
# # @auth # 账号密码的来源是ldap
# def transfer():
#     print('transfer')
#
#
# index=auth(index,'file')
# home=auth(home,'mysql')
# transfer=auth(transfer,'ldap')
#
# # index(1,2)
# # home('egon')
# # transfer()


# 山炮二
# def auth(db_type):
#     def deco(func):
#         def wrapper(*args, **kwargs):
#             name=input('your name>>>: ').strip()
#             pwd=input('your password>>>: ').strip()
#
#             if db_type == 'file':
#                 print('基于文件的验证')
#                 if name == 'egon' and pwd == '123':
#                     res = func(*args, **kwargs)
#                     return res
#                 else:
#                     print('user or password error')
#             elif db_type == 'mysql':
#                 print('基于mysql的验证')
#             elif db_type == 'ldap':
#                 print('基于ldap的验证')
#             else:
#                 print('不支持该db_type')
#
#         return wrapper
#     return deco
#
# deco=auth(db_type='file')
# @deco # 账号密码的来源是文件
# def index(x,y):
#     print('index->>%s:%s' %(x,y))
#
# deco=auth(db_type='mysql')
# @deco # 账号密码的来源是数据库
# def home(name):
#     print('home->>%s' %name)
#
# deco=auth(db_type='ldap')
# @deco # 账号密码的来源是ldap
# def transfer():
#     print('transfer')
#
#
# index(1,2)
# home('egon')
# transfer()


# 语法糖
def auth(db_type):
    def deco(func):
        def wrapper(*args, **kwargs):
            name = input('your name>>>: ').strip()
            pwd = input('your password>>>: ').strip()

            if db_type == 'file':
                print('基于文件的验证')
                if name == 'egon' and pwd == '123':
                    res = func(*args, **kwargs)  # index(1,2)
                    return res
                else:
                    print('user or password error')
            elif db_type == 'mysql':
                print('基于mysql的验证')
            elif db_type == 'ldap':
                print('基于ldap的验证')
            else:
                print('不支持该db_type')
        return wrapper
    return deco


@auth(db_type='file')  # @deco # index=deco(index) # index=wrapper
def index(x, y):
    print('index->>%s:%s' % (x, y))

@auth(db_type='mysql')  # @deco # home=deco(home) # home=wrapper
def home(name):
    print('home->>%s' % name)


@auth(db_type='ldap')  # 账号密码的来源是ldap
def transfer():
    print('transfer')

# index(1, 2)
# home('egon')
# transfer()




# 有参装饰器模板
def 有参装饰器(x,y,z):
    def outter(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return res
        return wrapper
    return outter

@有参装饰器(1,y=2,z=3)
def 被装饰对象():
    pass














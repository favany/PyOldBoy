"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""


# 精髓：可以把函数当成变量去用
# func=内存地址
def func():
    print('from func')


# 1、可以赋值
# f=func
# print(f,func)
# f()

# 2、可以当做函数当做参数传给另外一个函数
# def foo(x): # x = func的内存地址
#     # print(x)
#     x()
#
# foo(func) # foo(func的内存地址)

# 3、可以当做函数当做另外一个函数的返回值
# def foo(x): # x=func的内存地址
#     return x # return func的内存地址
#
# res=foo(func) # foo（func的内存地址）
# print(res) # res=func的内存地址
#
# res()

# 4、可以当做容器类型的一个元素
# l=[func,]
# # print(l)
# l[0]()

# dic={'k1':func}
# print(dic)
# dic['k1']()

# 函数对象应用示范：
# def login():
#     print('登录功能')
#
#
# def transfer():
#     print('转账功能')
#
#
# def check_banlance():
#     print('查询余额')
#
# def withdraw():
#     print('提现')
#
#
# def register():
#     print('注册')
#
# func_dic={
#     '1':login,
#     '2':transfer,
#     '3':check_banlance,
#     '4':withdraw,
#     '5':register
# }
#
# # func_dic['1']()
#
#
# while True:
#     print("""
#     0 退出
#     1 登录
#     2 转账
#     3 查询余额
#     4 提现
#     5 注册
#     """)
#     choice = input('请输入命令编号：').strip()
#     if not choice.isdigit():
#         print('必须输入编号，傻叉')
#         continue
#
#     if choice == '0':
#         break
#
#
#     if choice in func_dic:
#         func_dic[choice]()
#     else:
#         print('输入的指令不存在')
#
#     # if choice == '1':
#     #     login()
#     # elif choice == '2':
#     #     transfer()
#     # elif choice == '3':
#     #     check_banlance()
#     # elif choice == '4':
#     #     withdraw()
#     # else:
#     #     print('输入的指令不存在')


# 修正
def login():
    print('登录功能')


def transfer():
    print('转账功能')


def check_banlance():
    print('查询余额')


def withdraw():
    print('提现')


def register():
    print('注册')


func_dic = {
    '0': ['退出', None],
    '1': ['登录', login],
    '2': ['转账', transfer],
    '3': ['查询余额', check_banlance],
    '4': ['提现', withdraw],
    '5': ['注册', register]
}
# func_dic['1']()


while True:
    for k in func_dic:
        print(k, func_dic[k][0])

    choice = input('请输入命令编号：').strip()
    if not choice.isdigit():
        print('必须输入编号，傻叉')
        continue

    if choice == '0':
        break

    # choice='1'
    if choice in func_dic:
        func_dic[choice][1]()
    else:
        print('输入的指令不存在')

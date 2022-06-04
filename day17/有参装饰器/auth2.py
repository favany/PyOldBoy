def auth(login_type):
    def deco(func):
        def wrapper(*args, **kwargs):
            name = input("输入你的名字").strip()
            pwd = input("输入你的密码").strip()
            if login_type == "online":
                if name == "jun" and pwd == "123":
                    print("登陆成功")
                    res = func(*args, **kwargs)
                    return res
                else:
                    print("user or password error")
        return wrapper
    return deco


@auth("online")
def index():
    print("你好，欢迎在线登陆！")


@auth("offline")
def offline_index():
    print("你好，欢迎线下登陆！")


if __name__ == '__main__':
    index()
    offline_index()

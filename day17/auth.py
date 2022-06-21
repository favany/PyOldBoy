def auth(func, login_type):
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

@auth
def index():
    print("你好，欢迎登陆！")

if __name__ == '__main__':
    index()
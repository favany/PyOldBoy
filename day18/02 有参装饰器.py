# 一、知识储备

# def outer(func, x=3):
def outer(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res

    return wrapper


"""
由于语法糖🍬 @ 的限制，outer 函数只能有一个参数，
并且它只用来接收被装饰对象的内存地址
"""


@outer  # index = outer(index)
def index():
    ...


"""
偷梁换柱之后，
index 的（参数、返回值、属性）是什么样子，wrapper 的（参数、返回值、属性）就应该是什么样子

"""

# 二、有参装饰器


def auth(db_type):
    def deco(func):
        def wrapper(*args, **kwargs):
            name = input('your name >>>:').strip()
            pwd = input('your password>>>:').strip()
            # 从文件中取账号和密码
            if db_type == "file":
                if name == "mophia" and pwd == '123':
                    print('login successful!')
                    res = func(*args, **kwargs)
                else:
                    print('user or password error')
                return res
            elif  db_type == "MySQL":
                print("MySQL")
            elif  db_type == "ldap":
                print("ldap")
            else:
                print("不支持该类型")

        return wrapper
    return deco

@auth(db_type="file")
def index(x, y):
    print('index->>%s:%s' % (x, y))


# 原理

deco = auth(db_type="file")
@deco  # index = deco(index) = wrapper
def index(x, y):
    print('index->>%s:%s' % (x, y))


index(1, 2)


# 有参装饰器

def decorator(x, y, z):
  def outer(func):
      # @wraps(func)  # 将原函数的属性赋值给 wrapper，可加可不加
      def wrapper(*args, **kwargs):
          # 添加新功能
          res = func(*args, **kwargs)  # 调用原函数
          # 添加新功能
          return res
      return wrapper
  return outer

@decorator(1, y=2, z=3)
def index():
  pass

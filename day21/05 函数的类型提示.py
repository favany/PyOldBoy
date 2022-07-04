"""
@File      : 05 函数的类型提示.py
@Author    : 刘俊 mophia
@Email     : faaa@live.com
@Time      : 2022/7/2 5:23 PM

类型提示： Type hinting
"""


def register(name: str, age: int = 18, hobbies: tuple = ()) -> int:
    print(name, age, hobbies)
    return 111


register('mophia', 18, ('play', 'music', 12))


# 也可以写入提示信息
def register(name: "请传入名字"):
    return name


# 可以用以下方法查看提示信息
print(register.__annotations__)  # {'name': '请传入名字'}

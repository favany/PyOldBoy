import time


def func():
    time.sleep(3)
    print('hello world')


if __name__ == '__main__':
    res = func()  # 同步调用
    print('hahaha')
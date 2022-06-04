# @Time    : 2022/4/26 4:33 PM
# @Author  : 刘俊 Bingo
# @File    : 2.py.py
# @Info    :

import time

# time_calculator 是装饰器
def time_calculator(func):
    # func 是 index 方法 的内存地址
    def wrapper(*args, **kwargs):
        start = time.time()
        re = func(*args, **kwargs) # 写死了index
        stop = time.time()
        print("执行时间", stop - start)
        return re
    return wrapper

@time_calculator # index = time_calculator(index)
def index(x, y):
    time.sleep(3)
    print("index %s %s" % (x, y))
    return "Hello, world!"

if __name__ == '__main__':
    print(index(1, 2))

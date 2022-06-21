import time

# outer 是装饰器
def outer(func):
    # func 是 index 方法 的内存地址
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs) # 写死了index
        stop = time.time()
        print(stop - start)
    return wrapper

@outer # index = outer(index)
def index(x, y):
    time.sleep(3)
    print("index %s %s" % (x, y))





index(1, 2)


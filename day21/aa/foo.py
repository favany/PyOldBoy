x = 1


def get():
    print(x)


def change():
    global x  # 以定义阶段为准
    x = 0


print(__name__)


def say():
    print('我还活在内存中...')

# 1. 当 foo.py 运行时，__name__的值为 "__main__"
if __name__ == '__main__':
    print('文件被执行')
    change()
    get()


# 2. 当 foo.py 被当作模块导入时，__name__的值为模块名 "foo"
else:
    print('文件被导入')
    pass



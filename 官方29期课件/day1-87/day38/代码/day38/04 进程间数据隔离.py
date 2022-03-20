from multiprocessing import Process


money = 100


def task():
    global money  # 局部修改全局
    money = 666
    print('子',money)


if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    p.join()
    print(money)
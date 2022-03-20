from multiprocessing import Process
import time


def task(name, n):
    print('%s is running'%name)
    time.sleep(n)
    print('%s is over'%name)


if __name__ == '__main__':
    # p1 = Process(target=task, args=('jason', 1))
    # p2 = Process(target=task, args=('egon', 2))
    # p3 = Process(target=task, args=('tank', 3))
    # start_time = time.time()
    # p1.start()
    # p2.start()
    # p3.start()  # 仅仅是告诉操作系统要创建进程
    # # time.sleep(50000000000000000000)
    # # p.join()  # 主进程等待子进程p运行结束之后再继续往后执行
    # p1.join()
    # p2.join()
    # p3.join()
    start_time = time.time()
    p_list = []
    for i in range(1, 4):
        p = Process(target=task, args=('子进程%s'%i, i))
        p.start()
        p_list.append(p)
    for p in p_list:
        p.join()
    print('主', time.time() - start_time)
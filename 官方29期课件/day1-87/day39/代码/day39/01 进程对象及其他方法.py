from multiprocessing import Process, current_process
import time
import os


def task():
    # print('%s is running'%current_process().pid)  # 查看当前进程的进程号
    print('%s is running'%os.getpid())  # 查看当前进程的进程号
    # print('子进程的主进程号%s'%os.getppid())  # 查看当前进程的进程号
    time.sleep(30)


if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    p.terminate()  # 杀死当前进程
    # 是告诉操作系统帮你去杀死当前进程 但是需要一定的时间 而代码的运行速度极快
    time.sleep(0.1)
    print(p.is_alive())  # 判断当前进程是否存活
    """
    一般情况下我们会默认将
    存储布尔值的变量名
    和返回的结果是布尔值的方法名
    都起成以is_开头
    """
    print('主')
    # print('主',current_process().pid)
    # print('主',os.getpid())
    # print('主主',os.getppid())  # 获取父进程的pid号





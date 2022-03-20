# 第一种
from multiprocessing import Process
import time


def task(name):
    print('%s is running'%name)
    time.sleep(3)
    print('%s is over'%name)


if __name__ == '__main__':
    # 1 创建一个对象
    p = Process(target=task, args=('jason',))
    # 容器类型哪怕里面只有1个元素 建议要用逗号隔开
    # 2 开启进程
    p.start()  # 告诉操作系统帮你创建一个进程  异步
    print('主')
"""
windows操作系统下 创建进程一定要在main内创建
因为windows下创建进程类似于模块导入的方式
会从上往下依次执行代码
linux中则是直接将代码完整的拷贝一份
"""

# 第二种方式 类的继承
# from multiprocessing import Process
# import time
#
#
# class MyProcess(Process):
#     def run(self):
#         print('hello bf girl')
#         time.sleep(1)
#         print('get out!')
#
#
# if __name__ == '__main__':
#     p = MyProcess()
#     p.start()
#     print('主')













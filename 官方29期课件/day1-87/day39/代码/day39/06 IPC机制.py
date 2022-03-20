from multiprocessing import Queue, Process

"""
研究思路
    1.主进程跟子进程借助于队列通信
    2.子进程跟子进程借助于队列通信
"""
def producer(q):
    q.put('我是23号技师 很高兴为您服务')


def consumer(q):
    print(q.get())


if __name__ == '__main__':
    q = Queue()
    p = Process(target=producer,args=(q,))
    p1 = Process(target=consumer,args=(q,))
    p.start()
    p1.start()


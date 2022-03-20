from multiprocessing import Process, Queue, JoinableQueue
import time
import random


def producer(name,food,q):
    for i in range(5):
        data = '%s生产了%s%s'%(name,food,i)
        # 模拟延迟
        time.sleep(random.randint(1,3))
        print(data)
        # 将数据放入 队列中
        q.put(data)


def consumer(name,q):
    # 消费者胃口很大 光盘行动
    while True:
        food = q.get()  # 没有数据就会卡住
        # 判断当前是否有结束的标识
        # if food is None:break
        time.sleep(random.randint(1,3))
        print('%s吃了%s'%(name,food))
        q.task_done()  # 告诉队列你已经从里面取出了一个数据并且处理完毕了


if __name__ == '__main__':
    # q = Queue()
    q = JoinableQueue()
    p1 = Process(target=producer,args=('大厨egon','包子',q))
    p2 = Process(target=producer,args=('马叉虫tank','泔水',q))
    c1 = Process(target=consumer,args=('春哥',q))
    c2 = Process(target=consumer,args=('新哥',q))
    p1.start()
    p2.start()
    # 将消费者设置成守护进程
    c1.daemon = True
    c2.daemon = True
    c1.start()
    c2.start()
    p1.join()
    p2.join()
    # 等待生产者生产完毕之后 往队列中添加特定的结束符号
    # q.put(None)  # 肯定在所有生产者生产的数据的末尾
    # q.put(None)  # 肯定在所有生产者生产的数据的末尾
    q.join()  # 等待队列中所有的数据被取完再执行往下执行代码
    """
    JoinableQueue 每当你往该队列中存入数据的时候 内部会有一个计数器+1
    没当你调用task_done的时候 计数器-1
    q.join() 当计数器为0的时候 才往后运行
    """
    # 只要q.join执行完毕 说明消费者已经处理完数据了  消费者就没有存在的必要了
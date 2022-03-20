from multiprocessing import Queue

# 创建一个队列
q = Queue(5)  # 括号内可以传数字 标示生成的队列最大可以同时存放的数据量

# 往队列中存数据
q.put(111)
q.put(222)
q.put(333)
# print(q.full())  # 判断当前队列是否满了
# print(q.empty())  # 判断当前队列是否空了
q.put(444)
q.put(555)
# print(q.full())  # 判断当前队列是否满了

# q.put(666)  # 当队列数据放满了之后 如果还有数据要放程序会阻塞 直到有位置让出来 不会报错

"""
存取数据 存是为了更好的取
千方百计的存、简单快捷的取

同在一个屋檐下
差距为何那么大
"""

# 去队列中取数据
v1 = q.get()
v2 = q.get()
v3 = q.get()
v4 = q.get()
v5 = q.get()
# print(q.empty())
# V6 = q.get_nowait()  # 没有数据直接报错queue.Empty
# v6 = q.get(timeout=3)  # 没有数据之后原地等待三秒之后再报错  queue.Empty
try:
    v6 = q.get(timeout=3)
    print(v6)
except Exception as e:
    print('一滴都没有了!')

# # v6 = q.get()  # 队列中如果已经没有数据的话 get方法会原地阻塞
# print(v1, v2, v3, v4, v5, v6)

"""
q.full()
q.empty()
q.get_nowait()
在多进程的情况下是不精确
"""

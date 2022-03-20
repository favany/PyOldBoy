# from multiprocessing import Process
# import time
#
#
# class MyProcess(Process):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     def run(self):
#         print('hello bf girl')
#         time.sleep(1)
#         print(self.name)
#         print('get out!')
#
#
# if __name__ == '__main__':
#     p = MyProcess('egon')
#     p.start()
#     print('主')


s = (1)
print(type(s))  # <class 'int'>

s1 = ('hello')
print(type(s1))  # <class 'str'>

s2 = ()
print(type(s2))  # <class 'tuple'>
"""只要是容器类型 无论有几个元素(没有元素的情况无需加) 你都给我习惯性的把逗号加上"""







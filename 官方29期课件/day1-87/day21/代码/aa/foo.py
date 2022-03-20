print('模块foo==>')

__all__=['x',] # 控制*代表的名字有哪些

x=1

def get():
    print(x)

def change():
    global x
    x=0

def say():
    print('我还活在内存中呢。。。。')

# print(__name__) #
# 1、当foo.py被运行时，__name__的值为'__main__'
# 1、当foo.py被当做模块导入时，__name__的值为'foo'
# if __name__ == '__main__':
#     print('文件被执行')
#     get()
#     change()
# else:
#     # 被当做模块导入时做的事情
#     print('文件被导入')
#     pass



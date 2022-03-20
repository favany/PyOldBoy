from multiprocessing import Process
import time


def run():
    print('hello world')
    time.sleep(3)
    print('get out')


if __name__ == '__main__':
    p = Process(target=run)
    p.start()
    print('主')
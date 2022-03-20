from multiprocessing import Process
import time


def task(name):
    print('%s总管正在活着'% name)
    time.sleep(3)
    print('%s总管正在死亡' % name)


if __name__ == '__main__':
    p = Process(target=task,args=('egon',))
    # p = Process(target=task,kwargs={'name':'egon'})
    p.daemon = True  # 将进程p设置成守护进程  这一句一定要放在start方法上面才有效否则会直接报错
    p.start()
    print('皇帝jason寿终正寝')
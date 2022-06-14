import time

with open('access.log',mode='rt', encoding='utf8') as f:
    # 将指针跳到文件末尾
    # f.read()  # 错误
    f.seek(0, 2)

    while True:
        line = f.readline()
        if len(line) == 0:
            time.sleep(0.3)
        else:
            print(line)


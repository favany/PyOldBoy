"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""
from socket import *

client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8889))

while True:
    msg=input('请输入命令>>：').strip()
    if len(msg) == 0:continue
    client.send(msg.encode('utf-8'))

    res=client.recv(1024)
    print(res.decode('utf-8'))




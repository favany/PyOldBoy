"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""
import struct
from socket import *

client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8083))

while True:
    cmd=input('请输入命令>>：').strip()
    if len(cmd) == 0:continue
    client.send(cmd.encode('utf-8'))

    # 解决粘包问题思路：
    # 一、先收固定长度的头：解析出数据的描述信息，包括数据的总大小total_size
    header=client.recv(4)
    total_size=struct.unpack('i',header)[0]

    # 二、根据解析出的描述信息，接收真实的数据
    # 2、recv_size=0,循环接收，每接收一次，recv_size+=接收的长度
    # 3、直到recv_size=total_size，结束循环
    recv_size = 0
    while recv_size < total_size:
        recv_data=client.recv(1024)
        recv_size+=len(recv_data)
        print(recv_data.decode('utf-8'),end='')
    else:
        print()


# 粘包问题出现的原因
# 1、tcp是流式协议，数据像水流一样粘在一起，没有任何边界区分
# 2、收数据没收干净，有残留，就会下一次结果混淆在一起

# 解决的核心法门就是：每次都收干净，不要任何残留


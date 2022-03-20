"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""
import struct
import json
from socket import *

client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8083))

while True:
    cmd=input('请输入命令>>：').strip()
    if len(cmd) == 0:continue
    client.send(cmd.encode('utf-8'))

    # 接收端
    # 1、先手4个字节，从中提取接下来要收的头的长度
    x=client.recv(4)
    header_len=struct.unpack('i',x)[0]

    # 2、接收头，并解析
    json_str_bytes=client.recv(header_len)
    json_str=json_str_bytes.decode('utf-8')
    header_dic=json.loads(json_str)
    print(header_dic)
    total_size=header_dic["total_size"]

    # 3、接收真实的数据
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


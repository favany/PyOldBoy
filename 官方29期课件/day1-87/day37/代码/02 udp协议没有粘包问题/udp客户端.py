"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""

import socket

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.sendto(b'hello',('127.0.0.1',8080))
client.sendto(b'world',('127.0.0.1',8080))

client.close()
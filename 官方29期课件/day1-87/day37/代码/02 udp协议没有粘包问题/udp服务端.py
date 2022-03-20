"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""
import socket

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('127.0.0.1',8080))
res1=server.recvfrom(2) # b"hello"
print(res1)
res2=server.recvfrom(3) # b"world"
print(res2)

server.close()
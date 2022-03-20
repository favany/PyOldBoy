"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""
# 服务端应该满足两个特点：
# 1、一直对外提供服务
# 2、并发地服务多个客户端
import subprocess
import struct
from socket import *

server=socket(AF_INET,SOCK_STREAM)
server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) #就是它，在bind前加
server.bind(('127.0.0.1',8083))
server.listen(5)

#  服务端应该做两件事
# 第一件事：循环地从板连接池中取出链接请求与其建立双向链接，拿到链接对象
while True:
    conn,client_addr=server.accept()

    # 第二件事：拿到链接对象，与其进行通信循环
    while True:
        try:
            cmd=conn.recv(1024)
            if len(cmd) == 0:break
            obj=subprocess.Popen(cmd.decode('utf-8'),
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE
                             )

            stdout_res=obj.stdout.read()
            stderr_res=obj.stderr.read()
            total_size=len(stdout_res)+len(stderr_res)

            # 1、先发头信息（固定长度的bytes）：对数据描述信息
            # int->固定长度的bytes
            header=struct.pack('i',total_size)
            conn.send(header)

            # 2、再发真实的数据
            conn.send(stdout_res)
            conn.send(stderr_res)

        except Exception:
            break
    conn.close()





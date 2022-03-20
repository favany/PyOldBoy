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
import json
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

            # 1、制作头
            header_dic={
                "filename":"a.txt",
                "total_size":total_size,
                "md5":"123123xi12ix12"
            }

            json_str = json.dumps(header_dic)
            json_str_bytes = json_str.encode('utf-8')


            # 2、先把头的长度发过去
            x=struct.pack('i',len(json_str_bytes))
            conn.send(x)

            # 3、发头信息
            conn.send(json_str_bytes)
            # 4、再发真实的数据
            conn.send(stdout_res)
            conn.send(stderr_res)

        except Exception:
            break
    conn.close()





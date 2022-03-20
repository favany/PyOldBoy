"""
@作者: egon老湿
@微信:18611453110
@专栏: https://zhuanlan.zhihu.com/c_1189883314197168128
"""
import socketserver

class MyRequestHandle(socketserver.BaseRequestHandler):
    def handle(self):
        # 如果tcp协议，self.request=>conn
        print(self.client_address)
        while True:
            try:
                msg = self.request.recv(1024)
                if len(msg) == 0: break
                self.request.send(msg.upper())
            except Exception:
                break
        self.request.close()



#  服务端应该做两件事
# 第一件事：循环地从半连接池中取出链接请求与其建立双向链接，拿到链接对象
s=socketserver.ThreadingTCPServer(('127.0.0.1',8889),MyRequestHandle)
s.serve_forever()
# 等同于
# while True:
#     conn,client_addr=server.accept()
#     启动一个线程(conn,client_addr)

# 第二件事：拿到链接对象，与其进行通信循环===>handle
import socketserver

class MyRequestHanlde(socketserver.BaseRequestHandler):
    def handle(self):
        client_data=self.request[0]
        server=self.request[1]
        client_address=self.client_address
        print('客户端发来的数据%s' %client_data)
        server.sendto(client_data.upper(),client_address)


s=socketserver.ThreadingUDPServer(("127.0.0.1",8888),MyRequestHanlde)
s.serve_forever()
# 相当于:只负责循环地收
# while True:
#     data,client_addr=server.recvfrom(1024)
#     启动一个线程处理后续的事情(data,client_addr)








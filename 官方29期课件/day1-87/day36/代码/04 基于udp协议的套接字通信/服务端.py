import socket

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # 数据报协议=》udp协议

server.bind(('127.0.0.1',8081))

while True:
    data,client_addr=server.recvfrom(1024)
    server.sendto(data.upper(),client_addr)


server.close()






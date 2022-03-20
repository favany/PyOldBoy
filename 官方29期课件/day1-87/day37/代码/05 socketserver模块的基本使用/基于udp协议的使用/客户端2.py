import socket

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # 流式协议=》tcp协议

while True:
    msg=input('>>>: ').strip()
    client.sendto(msg.encode('utf-8'),('115.29.65.16',8888))
    res=client.recvfrom(1024)
    print(res)

client.close()
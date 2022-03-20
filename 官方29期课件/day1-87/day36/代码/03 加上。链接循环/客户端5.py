import socket

#1、买手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 流式协议=》tcp协议

#2、拨通服务端电话
phone.connect(('127.0.0.1',8080))

#3、通信
while True:
    msg=input("输入要发送的消息>>>: ").strip() #msg=''
    if len(msg) == 0:continue
    phone.send(msg.encode('utf-8'))
    print('======?')
    data=phone.recv(1024)
    print(data.decode('utf-8'))

#4、关闭连接(必选的回收资源的操作)
phone.close()
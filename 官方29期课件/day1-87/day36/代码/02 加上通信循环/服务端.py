import socket

# 1、买手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 流式协议=》tcp协议

# 2、绑定手机卡
phone.bind(('127.0.0.1',8083)) # 0-65535, 1024以前的都被系统保留使用

# 3、开机
phone.listen(5) # 5指的是半连接池的大小
print('服务端启动完成，监听地址为:%s:%s' %('127.0.0.1',8080))

# 4、等待电话连接请求：拿到电话连接conn
conn,client_addr=phone.accept()

# 5、通信：收\发消息
while True:
    try:
        data=conn.recv(1024) # 最大接收的数据量为1024Bytes，收到的是bytes类型
        if len(data) == 0:
            # 在unix系统洗，一旦data收到的是空
            # 意味着是一种异常的行为：客户度非法断开了链接
            break
        print("客户端发来的消息：",data.decode('utf-8'))
        conn.send(data.upper())
    except Exception:
        # 针对windows系统
        break

# 6、关闭电话连接conn（必选的回收资源的操作)
conn.close()

# 7、关机（可选操作）
phone.close()






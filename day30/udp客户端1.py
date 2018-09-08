from socket import *
ip_port=('127.0.0.1',8080)
buffer_size=1024

udp_client=socket(AF_INET,SOCK_DGRAM) #数据报

while True:
    msg=input('>>: ').strip()
    udp_client.sendto(msg.encode('utf-8'),ip_port)

    data,addr=udp_client.recvfrom(buffer_size)#基于UDP套接字的recvfrom如果收消息的时候自己的缓冲区为空，直接收到的消息为空
    # print(data.decode('utf-8'))
    print(data)
from socket import *
ip_port=('127.0.0.1',8080)
buffer_size=1024

udp_server=socket(AF_INET,SOCK_DGRAM) #数据报
udp_server.bind(ip_port)

#4个完全独立的数据包（因为UDP是基于数据报形式传输的）
data1=udp_server.recvfrom(10)
print('第一次',data1)

data2=udp_server.recvfrom(10)
print('第2次',data2)

data3=udp_server.recvfrom(10)
print('第3次',data3)

data4=udp_server.recvfrom(2)
print('第4次',data4)
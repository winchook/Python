from socket import *
ip_port=('127.0.0.1',8080)
back_log=5
buffer_size=1024

tcp_server=socket(AF_INET,SOCK_STREAM)
tcp_server.bind(ip_port)
tcp_server.listen(back_log)

conn,addr=tcp_server.accept()

data1=conn.recv(5)#这里的10表示一次只收取10个字节，所以会按照每次的收取大小来执行，如果设置较大的数字例如1024，则会一次性收取完客户端所传入的数据
print('第1次数据',data1)

data2=conn.recv(5)
print('第2次数据',data2)

data3=conn.recv(5)
print('第3次数据',data3)
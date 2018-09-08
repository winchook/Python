from socket import *
ip_port=('127.0.0.1',8080)
back_log=5
buffer_size=1024

udp_client=socket(AF_INET,SOCK_DGRAM)

while True:
    cmd=input('>>: ').strip()
    if not cmd:continue
    if cmd == 'quit':break

    udp_client.sendto(cmd.encode('utf-8'),ip_port)
    cmd_res,addr=udp_client.recvfrom(buffer_size)
    print('命令的执行结果是 ',cmd_res.decode('gbk'))

udp_client.close()

#UDP客户端可以直接执行，TCP客户端不能，TCP必须是有服务端在启动中
#UDP协议只管发，不管数据包是否被收到，所以不会发生粘包(上一个数据包没有显示完全，下一个数据包会接上一个内容继续显示)的现象，所以UDP协议不稳定

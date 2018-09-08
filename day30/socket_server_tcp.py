from socket import *
import subprocess
ip_port=('127.0.0.1',8080)
back_log=5
buffer_size=1024

tcp_server=socket(AF_INET,SOCK_STREAM)
tcp_server.bind(ip_port)
tcp_server.listen(back_log)

while True:
    conn,addr=tcp_server.accept()
    print('新的客户端连接',addr)
    while True:
        #收
        try:#用异常处理解决客户端在非正常关闭的情况下报的错误
            cmd=conn.recv(buffer_size)
            if not cmd:break#处理客户端正常关闭
            print('收到客户端命令',cmd)

            #执行命令，得到命令的运行结果cmd_res
            res=subprocess.Popen(cmd.decode('utf-8'),shell=True,
                                 stderr=subprocess.PIPE,
                                 stdout=subprocess.PIPE,
                                 stdin=subprocess.PIPE)
            err=res.stderr.read()
            if err:
                cmd_res=err
            else:
                cmd_res=res.stdout.read()

            #发
            if not cmd_res:#用if判断解决死循环的情况
                cmd_res='执行成功'.encode('gbk')
            conn.send(cmd_res)
        except Exception as e:
            print(e)#将打印"[WinError 10054] 远程主机强迫关闭了一个现有的连接。"
            break


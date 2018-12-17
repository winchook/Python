# 基于paramiko模块，安装pip3 install paramiko
# 基于requests模块，来采集及提交数据
import paramiko
import requests

#########获取当天未采集的主机名########
# result = requests.get('http://127.0.0.1:8000/assets.html')
# # 暂时认为result是列表类型的
# result = ['c1.com','c2.com']

#########通过paramiko连接远程服务器，执行命令##########
# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='127.0.0.1', port=22, username='root', password='123')

# 执行命令
stdin, stdout, stderr = ssh.exec_command('df -hT')
# 解释：stdin.write('Y')使用在交互的对话模块

# 获取命令结果
result = stdout.read()
# 输出df -hT的结果
print(result)
# 关闭连接
ssh.close()

# 格式化数据
#data_dict = {}

###########发送数据########
# requests.post('http://127.0.0.1:8000/assets.html',data=data_dict)


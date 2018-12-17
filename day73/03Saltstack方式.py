# 1. centos7安装saltstack
# yum -y install https://repo.saltstack.com/yum/redhat/salt-repo-latest-2.el7.noarch.rpm
# yum clean expire-cache

# master节点安装在k-node01
# yum -y install salt-master

# slave节点安装在k-node02
# yum -y install salt-minion

# 修改master配置文件
# interface: 172.31.0.15

# 修改slave配置文件
# master: 172.31.0.15

# 启动master节点
# systemctl start salt-master
# 启动slave节点
# systemctl start salt-minion


"""
        Master： yum install salt-master
       Master准备：
            a. 配置文件，监听本机IP
                vim /etc/salt/master
                interface: 本机IP地址
            b. 启动master
                systemctl start salt-master


        Slave：  yum install salt-minion
        Slave准备：
            a. 配置文件，连接那个master
                vim /etc/salt/minion
                master: 远程master地址
            b. 启动slave
                systemct start salt-slave

2. 创建关系
    查看
    Master：salt-key -L
        Accepted Keys:
        Denied Keys:
        Unaccepted Keys:
            k-node02
        Rejected Keys:
    接受
    Master执行命令：salt-key -a k-node02
        Accepted Keys:
            k-node02
        Denied Keys:
        Unaccepted Keys:
        Rejected Keys:


3. 执行命令
    master：
        salt 'k-node02' cmd.run  'ifconfig'

    import salt.client
    local = salt.client.LocalClient()
    result = local.cmd('c2.salt.com', 'cmd.run', ['ifconfig'])

    print(type(result))
    <type 'dict'>

"""
# ################## 获取当天未采集主机名 ##################
# result = requests.get('http://www.127.0.0.1:8000/assets.html')
# result = ['c1.com','c2.com']


# ################## 远程服务器执行命令 ##################
# import subprocess
# result = subprocess.getoutput("salt 'c1.com' cmd.run  'ifconfig'")
#
# import salt.client
# local = salt.client.LocalClient()
# result = local.cmd('c2.salt.com', 'cmd.run', ['ifconfig'])


# ##################  发送数据 ##################
# requests.post('http://www.127.0.0.1:8000/assets.html',data=data_dict)
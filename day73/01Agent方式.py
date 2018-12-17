import subprocess
import requests
# 如果没有上面的模块，使用命令安装
# pip3 install requests

###########采集数据###########
# 接收字符串格式的命令，执行命令并返回执行结果，其功能类似于os.popen(cmd).read()和commands.getoutput(cmd)
# result = subprocess.getoutput('ipconfig')
# print(result)
# result正则处理获取想要的数据

# 整理资产信息
# data_dict ={
#     'nic':{},
#     'disk':{},
#     'mem':{}
# }

###########发送数据########
# requests.post('http://127.0.0.1:8000/assets.html',data=data_dict)
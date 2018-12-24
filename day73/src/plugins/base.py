from conf import settings

class BasePlugin(object):
    def __init__(self):
        mode_list = ['SSH','Salt','Agent']
        if settings.MODE in mode_list:
            self.mode = settings.MODE#这里的self是指在程序开始时obj = DiskPlugin()，就已经验证了
        else:
            raise Exception('配置文件错误')
    def ssh(self,cmd):
        pass
    def agent(self,cmd):
        pass
    def salt(self,cmd):
        pass
    def shell_cmd(self,cmd):
        if self.mode == 'SSH':
            ret = self.ssh(cmd)
        elif self.mode == 'Salt':
            ret = self.salt(cmd)
        else:
            ret = self.agent(cmd)
        return ret
    def execute(self):
        ret = self.shell_cmd('查看平台命令')
        if ret == 'win':
            return self.windows()#这里的return表示有返回值，可以在result = obj.execute()拿到结果
        elif ret == 'linux':
            return self.linux()
        else:
            raise Exception('只支持windows和linux')

        self.linux()
    def linux(self):
        raise Exception('....')
    def windows(self):
        raise Exception('....')
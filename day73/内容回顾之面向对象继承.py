
class Bbh():
    def server(self):
        self.sz()
    def sz(self):
        self.xiaowen()

class Mr(Bbh):#Mr继承了Bbh
    def sz(self):
        print('sz')
    def xiaowen(self):
        self.process_request()
class Yun():
    def process_request(self):
        print('yun')

class Zzc(Yun,Mr):#Zzc继承了Yun和Mr
    pass

obj = Zzc()
obj.server()
# 输出结果：sz

class Bbh():
    def server(self):
        self.sz()
    def sz(self):
        self.xiaowen()

class Mr(Bbh):#Mr继承了Bbh
    # def sz(self):
    #     print('sz')
    def xiaowen(self):
        self.process_request()
class Yun():
    def process_request(self):
        print('yun')

class Zzc(Yun,Mr):#Zzc继承了Yun和Mr
    pass

obj = Zzc()
obj.server()
# 输出结果：yun



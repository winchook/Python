# 采集资产：三种不同的形式

class BasePlugin(object):
    def __init__(self):
        pass
    def execute(self):
        self.linux()
    def linux(self):
        raise Exception('....')

class DiskPlugin(BasePlugin):
    def linux(self):
        return '硬盘'
    def execute(self):
        pass

obj = DiskPlugin()
obj.execute()

# 执行顺序
#1、 obj = DiskPlugin()实例化需要执行DiskPlugin()的__init__方法
#    没有，则去BasePlugin里面找__init__方法
#2、 在BasePlugin里面找到了__init__方法，则执行：
#    def __init__(self):
#        pass
#    这时obj拿到的是DiskPlugin的对象（只需要确认obj = DiskPlugin()这里括号
#    是谁就是谁的对象，也就是说哪个类加的括号前面的对象就是谁）
#3、  继续执行obj.execute()，先去class DiskPlugin(BasePlugin):里面找
#    找到了def execute(self):则执行，这时def execute(self):里面的self
#    指的是刚刚实例化的对象。
#    因为优先在自己里面的类来找，下面的情况是，如果在自己类class DiskPlugin(BasePlugin):
#    没找到def execute(self):，则会往上找class BasePlugin(object):里面的def execute(self):
#    方法，这时的self指的还是DiskPlugin里面的对象，因为至始至终只实例化了一个对象
#总结：只需要关注obj = DiskPlugin()实例化时候的类是谁，就从那个类进行找
# 定义三种获取数据的模式
MODE = "Agent" # Salt,SSH
PLUGINS = {
    'disk':'src.plugins.disk.DiskPlugin',
    'mem':'src.plugins.mem.MemPlugin',
    'nic':'src.plugins.nic.NicPlugin',
}
# from .plugins.disk import DiskPlugin
# from .plugins.mem import MemPlugin
# from .plugins.nic import NicPlugin

from conf import settings
def pack():
    # obj1 = DiskPlugin()
    # disk_info = obj1.execute()
    # obj2 = MemPlugin()
    # mem_info = obj2.execute()
    # obj3 = NicPlugin()
    # nic_info = obj3.execute()
    #
    # respoonse = {
    #     'nic':nic_info,
    #     'mem':mem_info,
    #     'disk':disk_info
    # }
    response = {}
    for k,v in settings.PLUGINS.items():
        response[k] = v().execute()
    return respoonse
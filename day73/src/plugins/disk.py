from .base import BasePlugin

class DiskPlugin(BasePlugin):
    def linux(self):
        return '硬盘'
    def windows(self):
        pass
from .base import BasePlugin

class NicPlugin(BasePlugin):
    def linux(self):
        output = self.shell_cmd('asdf')
        return output
    def windows(self):
        output = self.shell_cmd('asdf')
        return output
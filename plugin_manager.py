from pluginmanager import PluginInterface
import sys

class PluginManager:
    def __init__(self) -> None:
        self.interface = PluginInterface()
        self.interface.set_plugin_directories('plugins')
        self.interface.collect_plugins()
    
    def get_plugins(self):
        return self.interface.get_instances()
        
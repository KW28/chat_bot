from pluginmanager import IPlugin

from inspect import isclass

def plugin(name):
    
    def create_plugin(func):
        plugin_class = type(func.__name__, PluginModel.__bases__, dict(PluginModel.__dict__))
        if isclass(func):
            func = func()
        
        plugin_class.name = name
        plugin_class._backend = (func,)
        
        return plugin_class
    return create_plugin



class PluginModel(IPlugin):
    
    def __init__(self, *args):
        super(IPlugin, self).__init__()
        
    def run(self, string, *args):
        self._backend[0](string)
        

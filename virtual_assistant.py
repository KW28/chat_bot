from plugin_manager import PluginManager
from text_colors import *
from cmd import Cmd
from functools import partial
import os

class VirtualAssistant(Cmd):
    PROMPT_CHAR = '~> '
    print(f'{LIGHT_BLUE}Hi, How Can I Help You?')
    prompt = PROMPT_CHAR
    
    def __init__(self) -> None:
        Cmd.__init__(self)
        self.manager = PluginManager()
        self.plugins = self.manager.get_plugins()
        self.activate_plugins()
        
    def precmd(self, line: str):
        os.system('clear')
        line = line.replace(',', '')
        line = line.replace('?', '')
        line = line.replace('!', '')
        line = line.lower()
        line = line.strip()
        
        return line
    
    def postcmd(self, stop: bool, line: str) -> bool:
        print('\nWhat else?')
    
    def run(self):
        self.cmdloop()
        
    def activate_plugins(self):
        for plugin in self.plugins:
            setattr(VirtualAssistant, 'do_' + plugin.name, plugin.run)
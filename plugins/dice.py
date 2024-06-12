from plugin import plugin
from data_structures import PDA
from data_structures import BinTree
from random import randint
import sys


@plugin('roll')
def roll(line):
    line = line.replace(' ', '')
    line = [*line]
    line.append('')
    
    roller = Roll(line)
    roller.run()
    
    

class Roll(PDA):
    def __init__(self, tokens) -> None:
        super().__init__()
        self.result = None
        self.tokens = tokens
        self.syntax_tree = None
        
    def run(self):
        for item in self.tokens:
            self.transition(item)
        
    def transition(self, token):
        if self.state == 'q0':
            
            if token.isdigit():
                self.stack.append('digit')
    
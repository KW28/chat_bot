from typing import Any
from plugin import plugin
from data_structures import PDA
from random import randint

@plugin('roll')
class Roll(PDA):
    def __init__(self) -> None:
        super().__init__()
        self.result = ''
        #self.syntax_tree = None
        
    def run(self):
        for item in self.tokens:
            self.transition(item)
        
    def transition(self, token):
        if self.state == 'q0':
            
            if token.isdigit() and self.peek() == 'Z':
                self.push('D')
                self.result += token
                self.state = 'q0'
                return 
                
            if token.isdigit() and self.peek() == 'D':
                self.result += token
                self.state = 'q0'
                return 
            
            if token == 'd' and self.peek() == 'D':
                self.pop()
                self.push('C')
                self.result += token
                self.state = 'q1'
                return 
            
            if token == 'd' and self.peek() == 'Z':
                self.push('C')
                self.result += token
                self.state = 'q1'
                return 
        
            print('Unexpected token in state q0.')
            
        if self.state == 'q1':
            
            if token.isdigit() and self.peek() == 'C':
                self.pop()
                self.push('D')
                self.result += token
                self.state = 'q2'
                return 
            
            print('Unexpected token in state q1.')
        
        if self.state == 'q2':
            
            if token.isdigit() and self.peek() == 'D':
                self.result += token
                return 
            
            if token in ('+', '-') and self.peek() == 'D':
                self.pop()
                self.push('M')
                self.result += token
                self.state = 'q3'
                return 
        
            print('Unexpected token in state q2.')
            
        if self.state == 'q3':
            print(token, self.peek())
            
            if token.isdigit() and self.peek() == 'M':
                self.pop()
                self.push('D')
                self.result += token
                self.state = 'q4'
                return
            
            print('Unexpected token in state q3.')
            
        if self.state == 'q4':
            
            if token.isdigit() and self.peek == 'D':
                self.result += token
                return
            
            if self.peek() == 'Z':
                self.state = 'qf'
            
            print('Unexpected token in state q4.')
                
        if self.state == 'qf':
            raise Exception('Had an token while in state qf')
        

    def __call__(self, line):
        line = line.replace(' ', '')
        line = [*line]
        #line.append('')
        print(line)
        
        for token in line:
            self.transition(token)
        
        print(self.result)
        self.reset()
        self.result = ''

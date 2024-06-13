
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)
    
    def clear(self):
        self.items = []


class PDA(Stack):
    def __init__(self, end_symbol='Z') -> None:
        super().__init__()
        self.end_symbol = end_symbol
        self.state = 'q0'
        self.push(end_symbol)
        
    def reset(self):
        self.clear()
        self.push(self.end_symbol)
        self.state = 'q0'
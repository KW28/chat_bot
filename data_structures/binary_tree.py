

# TODO
        
class Node:
    def __init__(self, value, parent) -> None:
        self.value = value
        self.parent = parent
        self.left_child = None
        self.right_child = None
        
    def create_child(self, direction, value):
        child = Node(value, self)
        
        if direction == 'left':
            self.left_child = child
            
        if direction == 'right':
            self.right_child = child
    
    def __str__(self, level=0):
        if level == 0:
            ret = repr(self.value)
        else:
            ret =  "\n" + "     " * (level - 1) + "|" + "----" + repr(self.value)
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
    
    def get_root(self):
        if self.parent == None:
            return self
        return self.parent.get_root()
    
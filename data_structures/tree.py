import sys
sys.dont_write_bytecode = True
class Node:
    def __init__(self, value, parent) -> None:
        self.value = value
        self.parent = parent
        self.children = []
        
    def has_child(self):
        if self.children == []:
            return False
        else:
            return True
        
    def create_child(self, value=None):
        new_child = Node(value, self)
        self.children.append(new_child)
        return new_child
    
    def remove_child(self, target):
        self.children.pop(target)
    
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
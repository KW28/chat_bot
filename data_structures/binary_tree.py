
class BinaryTree:
    def __init__(self, initial_value=None) -> None:
        self.root_node = Node(initial_value, None)
        self.current_node = self.root_node
        
class Node:
    def __init__(self, value, parent, left_child=None, right_child=None) -> None:
        self.value = value
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child
        
    def create_left_child(self, value):
        if self.left_child != None:
            self.left_child = Node(value, self)
        else:
            raise Exception('Cannot create left child. Left child already exists')
        
    def create_right_child(self, value):
        if self.right_child != None:
            self.right_child = Node(value, self)
        else:
            raise Exception('Cannot create left child. Left child already exists')
    
    def remove_child(self, target):
        if target == 'left':
            self.left_child = None
        elif target == 'right':
            self.right_child = None
        elif target == 'both':
            self.left_child = None
            self.right_child = None
        else:
            raise Exception(f'Target invalid. Target is {target}')
            
    
    def calapse_children(self, new_value):
        self.value = new_value
        self.remove_child('both')
        
    
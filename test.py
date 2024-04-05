from data_structures import tree as DataTree
from plugins import dice
import sys

sys.dont_write_bytecode = True

def tree_display():
    root = DataTree.Node(0, None)
    child1 = root.create_child(1)
    child2 = root.create_child(2)
    child3 = child1.create_child(3)
    child4 = child1.create_child(4)
    print(root)
    
def roll_test():
    sys.dont_write_bytecode = True
    final_dict = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6':0}
    
    for i in range(1000000):
        result = str(dice.roll('1d6')[0])
        value = final_dict[result] + 1
        final_dict.update({result: value})
    
    print(final_dict)
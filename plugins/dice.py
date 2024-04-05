from plugin import plugin
from data_structures import tree as DataTree
from constant_values import SPLIT_CHARACTER, END_CHARACTER
from random import randint
import sys


@plugin('roll')
def roll(line):
    sys.dont_write_bytecode = True
    letters = [*line]
    for i in range(len(letters)):
        if letters[i] == 'd':
            letters[i] = SPLIT_CHARACTER
    letters.append(END_CHARACTER)
    root_node = DataTree.Node(None, None)
    complete_tree = create_parse_tree(root_node, letters, 0)
    print(evaluate_parse_tree(complete_tree.get_root()))
    

def create_parse_tree(node, letters, i):
    letter = letters[i]
    
    #Base case
    if letter == END_CHARACTER:
        return node
    
    if node.parent == None:
        child = node.create_child()
        return create_parse_tree(child, letters, i)
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # If Token is a "d"
    
    if letter == SPLIT_CHARACTER:
        
        if node.value == None:
            node.value = SPLIT_CHARACTER
            child = node.create_child()
            return create_parse_tree(child, letters, i+1)
        
        if node.value.isdigit():
            if node.parent.value == None:
                node.parent.value = SPLIT_CHARACTER
                sibling = node.parent.create_child()
                return create_parse_tree(sibling, letters, i+1)
            
        raise Exception('Given token was a "d" and both self value and parent value were filled.')
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #If token is a number

    if letter.isdigit():
        
        if node.value != None:
            
            if node.value.isdigit():
                node.value += letter
                return create_parse_tree(node, letters, i+1)
            
            raise Exception('Given a digit but current value is not None or a digit')
        
        if node.parent.value != SPLIT_CHARACTER:
            child = node.create_child(letter)
            return create_parse_tree(child, letters, i+1)
        
        node.value = letter
        return create_parse_tree(node, letters, i+1)
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #If token is a space
    
    if letter == ' ':
        if node.value != None:
            if node.value.isdigit():
                if node.parent.value != None:
                    return create_parse_tree(node.get_root(), letters, i+1)
            
            
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #If anything else is inputed
    
    return create_parse_tree(node, letters, i+1)

def evaluate_parse_tree(node):
    
    if node.parent == None:
        final_rolls = []
        for child in node.children:
            final_rolls.append(evaluate_parse_tree(child))
        return final_rolls
        
    if node.value == SPLIT_CHARACTER:
        if len(node.children) == 1:
            return randint(1, int(node.children[0].value))
        
        return randint(int(node.children[0].value), int(node.children[1].value))
from data_structures import tree as DataTree

def tree_display():
    root = DataTree.Node(0, None)
    child1 = root.create_child(1)
    child2 = root.create_child(2)
    child3 = child1.create_child(3)
    child4 = child1.create_child(4)
    print(root)
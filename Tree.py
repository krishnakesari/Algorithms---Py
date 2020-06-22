
# Trees are built as nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

n1 = Node("root node")
n2 = Node("left child node")
n3 = Node("right child node")
n4 = Node("left grandchild node")

n1.left_child = n2
n1.right_child = n3
n2.left_child = n4

current = n1
while current:
    print(current.data)
    current = current.left_child

# Binary Tree: Should have a maximum of two children
# Binart search trees: left side > 5 and right side < 5

# Binary search tree implementation
class Tree:
    def __int__(self):
        self.root_node = None


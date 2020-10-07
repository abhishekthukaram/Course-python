"""
Tree Implementation
"""

"""
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_left(self, data):
        if self.left is None:
            self.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = self.left
            self.left = new_node


tree= Node(1)
print dir(tree)
tree.insert_left(2)
print tree.data
print tree.left.data
print tree.right
"""

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self, root):
        self.root = Node(root)


output =BinaryTree(3)
output.root.left = Node(2)
output.root.right = Node(4)
output.root.left.left = Node(5)
output.root.left.right = Node(6)
output.root.right.left = Node(7)
output.root.right.right = Node(8)
print (output.root.right.right.data)

"""
class Node():
    def __init__(self, data):
        self.data =data
        self.left = None
        self.right = None
"""

"""
Let's modify the Tree constructor so that it takes an input that initializes the root node. Choose between one of two 
options: 1) the constructor takes a Node object
2) the constructor takes a value, then creates a new Node object using that value.
"""

"""
Option 1: 

class Nodewithvalue():
    def __init__(self, data=None):
        self.value =data
        self.left = None
        self.right=None

    def get_value(self):
        return self.value

    def set_value(self,value):
        self.value = value

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_left_child(self,node):
        self.left= node

    def set_right_child(self, node):
        self.right = node

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None


class Tree():
    def __init__(self, node):
        self.root = node

    def get_root_node(self):
        return self.root
"""

"""
Option 2: 
"""
class Node():
    def __init__(self, data=None):
        self.value =data
        self.left = None
        self.right=None

    def get_value(self):
        return self.value

    def set_value(self,value):
        self.value = value

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_left_child(self,left):
        self.left= left

    def set_right_child(self, right):
        self.right = right

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None


class Tree():
    def __init__(self, value):
        self.root = Node(value)

    def get_root_node(self):
        return self.root


tree = Tree("Apple")
print (dir(tree.get_root_node()))
print ("Root is:",tree.get_root_node().value)
tree.get_root_node().set_left_child(Node("banana"))
print ("Root's Left Child:",tree.get_root_node().get_left_child().value)
tree.get_root_node().set_right_child(Node("Orange"))
print ("Root's Right Child:",tree.get_root_node().get_right_child().value)
tree.get_root_node().get_left_child().set_left_child(Node("Dates"))
print("Root's left grandchild:",tree.get_root_node().get_left_child().get_left_child().value)
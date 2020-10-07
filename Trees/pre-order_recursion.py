class Node():
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

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


#tree = Tree(Node("Apple"))


def pre_order(tree):
    visit_order = []
    root = tree.get_root_node()

    def traverse(node):
        if node:
            visit_order.append(node.get_value())
            """Visit Left"""
            traverse(node.get_left_child)
            """Visit Right"""
            traverse(node.get_right_child)
    traverse(root)
    return visit_order

"""
def in_prder(tree):
    visit_order = []
    root = tree.get_root_node()

    def traverse(node):
        if node:
            traverse(node.get_left_child)
            visit_order.append(node.get_value())
            traverse(node.get_right_child)
    traverse(root)
    return visit_order
"""


def in_order(tree):
    visit_order = []
    if tree:
        in_order(tree.left)
        print tree.value,
        in_order(tree.right)


def post_prder(tree):
    visit_order = []
    root = tree.get_root_node()

    def traverse(node):
        if node:
            traverse(node.get_left_child)
            traverse(node.get_right_child)
            visit_order.append(node.get_value)

    traverse(root)
    return visit_order


tree = Node("Apple")
#tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
in_order(tree)

tree = Node("Apple")
#print dir(tree.get_root_node())
#print "Root is:",tree.get_root_node().value
tree.left = Node("banana")
#print "Root's Left Child:",tree.get_root_node().get_left_child().value
tree.right = Node("Orange")
#print "Root's Right Child:",tree.get_root_node().get_right_child().value
tree.left.left = Node("Dates")
in_order(tree)

class Node():
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


"""
class Tree():
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def set_root(self, value):
        if self.root is None:
            self.root = Node(value)

    def compare(self,node,new_node):
        if new_node.value < node.value:
            return -1
        elif new_node.value > node.value:
            return 1
        return 0
"""


def insert(root, node):
    #newnode = Node(newvalue)
    if root is None:
        root= node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right,node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def search(root, value):
    print "root is :",root.data
    print "value is", value
    if root.data == value:
        return True
    elif root.data>value:
        if root.left is not None:
            return search(root.left, value)
        else:
            return False
    else:
        if root.right is not None:
            return search(root.right, value)
        else:
            return False



def inorder(root):
    if root:
        inorder(root.left)
        print root.data
        inorder(root.right)


r = Node(50)
insert(r,Node(30))
#print r.left.data
#print search(r, 30)
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))
print search(r, 200)
#insertion(root, 30)
#insertion(root, 80)
#insertion(root, 40)
#inorder(r)

"""
#print dir(root.right)
print root.data
print root.left.data
print root.right.data
print root.right.right.data
"""













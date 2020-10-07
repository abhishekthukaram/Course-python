"""
Task 01 build a node
"""


class EmptyNode():
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None


buildnode = EmptyNode()
print "value:", (buildnode.value)
print "left:", buildnode.left
print "right:", buildnode.right

"""
add a constructor that takes the value as a parameter
Copy what you just made, and modify the constructor so that it takes in an optional value, which it assigns as the
node's value. Otherwise, it sets the node's value to None.
"""


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


newnode0 = Nodewithvalue("Apple")
print "Has Left Child:",newnode0.has_left_child()
newnode1 = Nodewithvalue("Orange")
newnode2 = Nodewithvalue("Banana")
print newnode0.get_value()
newnode0.set_left_child(newnode1)
newnode0.set_right_child(newnode2)
print "HAs Left Child:",newnode0.has_left_child()
newnode1.set_value("Orange")
print "value:", newnode0.value
print "value-Left:", newnode0.left.value
print "value-Right:", newnode0.right.value
print "Has Right Child:",newnode0.has_right_child()




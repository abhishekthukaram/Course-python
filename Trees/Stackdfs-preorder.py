class Stack():
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if len(self.items) ==0:
            return "Stack is empty"
        else:
            self.items.pop()

    def stackisempty(self):
        return self.items == []

    def topofstack(self):
        return self.items[-1]


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


"""
For Tracking Purpose
"""


class State():
    def __init__(self, node):
        self.node = node
        self.visited_left = False
        self.visited_right = False

    def get_node(self):
        return self.node

    def get_visited_left(self):
        return self.visited_left

    def get_visited_right(self):
        return self.visited_right

    def set_visited_left(self):
        self.visited_left = True

    def set_visited_right(self):
        self.visited_right = True


tree = Tree()


def preorderwithStack(tree):
    visit_order = list()
    stack = Stack()
    node= tree.get_root_node()
    visit_order.append(node.get_value())
    state = State(node)
    stack.push(state)
    count =0
    while node:
        if node.has_left_child() and not state.get_visited_left():
            state.set_visited_left()
            node = node.get_left_child()
            visit_order.append(node.get_value())
            state = State(node)
            stack.push(state)
        elif node.has_right_child() and not state.get_visited_right():
            state.set_visited_right()
            node = node.get_right_child()
            visit_order.append(node.get_value)
            state = State(node)
            stack.push(state)
        else:
            stack.pop()
            if not stack.stackisempty():
                state = stack.topofstack()
                node = state.get_node()
            else:
                node = None



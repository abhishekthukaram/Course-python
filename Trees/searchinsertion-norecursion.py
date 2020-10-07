class Node():
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def set_value(self, data):
        self.value = data

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_left_child(self, data):
        self.left = data

    def set_right_child(self, data):
        self.right = data


class Tree():
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def insertion(self, new_value):
        new_node = Node(new_value)
        node = self.get_root()
        if new_node is None:
            self.root = new_node
        while True:
            if node.get_value() == new_node.get_value():
                node.set_value(new_node.get_value())
            elif node.get_value < new_node.get_value():
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    break
            else:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    break

class Node:
    def __init__(self,data):
        self.data =data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def deletion(self, data):
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return
        previous_node = None
        while current_node and current_node.data != data:
            previous_node= current_node
            current_node=current_node.next
        if current_node is None:
            return "Element not found"
        else:
            previous_node.next = current_node.next
            current_node= None




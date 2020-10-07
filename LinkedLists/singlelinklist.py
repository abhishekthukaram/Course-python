class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head
        while current is not None:
            print (current.data)
            current = current.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return "Added New Node"
        node_iterator = self.head
        while node_iterator.next is not None:
            node_iterator = node_iterator.next
        node_iterator.next = new_node

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head= new_node

    def insertion(self, previous_node, data):
        new_node = Node(data)
        if not previous_node:
            return "Node not present in List"
        else:
            new_node.next = previous_node.next
            previous_node.next = new_node

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

    def deletebyposition(self, pos):
        current_node =self.head
        if pos ==0:
            self.head = current_node.next
            current_node = None
            return
        prev = None
        count =0
        while current_node and count!=pos:
            pre = current_node
            current_node = current_node.next
            count+=1
        if current_node is None:
            return "No element"
        prev.next = current_node.next
        current_node= None

    def lengthlinklist(self):
        count = 0
        current = self.head
        while current is not None:
            count+=1
            current = current.next
        return count

    def reverselinklist(self):
        current_node = self.head
        prev_node = None
        while current_node is not None:
            next = current_node.next
            current_node.next = prev_node
            prev_node=current_node
            current_node =next
        self.head = prev_node


output = LinkedList()
output.append("Abhi")
output.append("Tabhi")
output.append("Tubby")
output.prepend("MU")
output.insertion(output.head.next.next,"DEvil")
output.deletion("Tabhi")

print(output.print_list())
print(output.lengthlinklist())
print(output.reverselinklist())
print(output.print_list())

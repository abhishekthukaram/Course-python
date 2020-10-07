class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head):
        self.head = head

    def append(self,newelement):
        currentnode= self.head
        if currentnode:
            while currentnode.next is not None:
                currentnode= currentnode.next
            currentnode.next = Node(newelement)
        else:
            self.head= Node(newelement)

    def printall(self):
        current_nodes= self.head
        while current_nodes is not None:
            print(current_nodes.value)
            current_nodes = current_nodes.next


node1 = Node("3")
node2= Node("2")
node3= Node("1")

node1.next= node2
node2.next = node3
nodeout= LinkedList(node1)
nodeout.append(4)
nodeout.printall()


"""
head = node1
current_node = head
while current_node is not None:
    print current_node.value
    current_node=current_node.next
"""
"""
first = Node(1)
second = Node(2)
first.next= second
third = Node(3)
second.next = Node(3)
print third.next
"""
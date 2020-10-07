class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(2)
print head.value
head.next = Node(3)
print head.next
print head.next.value
print head.next.next
"""
head = Node(2)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = Node(1)
head.next.next.next.next =Node(5)

def createlinkiedlist(head):
    current_node = head
    while current_node is not None:
        print current_node.value
        current_node=current_node.next


createlinkiedlist(head)
 
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = Node(1)
head.next.next.next.next =Node(5)
print (head.next.next.next.next.next)

def createfrominputlist(input_list):
    head = None
    tail = None
    for value in input_list:
        if head is None:
            head = Node(value)
            tail = head
        else:
            tail.next = Node(value)
            tail = tail.next
    return head
"""
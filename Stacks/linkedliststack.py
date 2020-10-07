"""
Implement a stack using a linked list
"""


class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None


class Stack():
    def __init__(self):
        self.head = None
        self.num_elements =0

    def push(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements+=1

    def sizeofstack(self):
        if self.head is None:
            return "Stack is empty"
        else:
            return self.num_elements

    def is_empty(self):
        return self.num_elements ==0

    def pop(self):
        if self.head is None:
            return None
        else:
            value = self.head.data
            self.head = self.head.next
            self.num_elements-=1
        return value



stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
print stack.sizeofstack()
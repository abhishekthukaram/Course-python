"""
Building a Stack in Python
"""


class Stack:
    def __init__(self):
        self.stacklist = []

    # TODO: Initialize the Stack

    def size(self):
        return len(self.stacklist)

    # TODO: Check the size of the Stack

    def push(self, item):
        self.stacklist.append(item)

    # TODO: Push item onto Stack

    def pop(self):
        if len(self.stacklist)==0:
            return "Stack is empty"
        else:
            self.stacklist.pop()


MyStack = Stack()
MyStack.push("Web Page 1")
MyStack.push("Web Page 2")
MyStack.push("Web Page 3")
MyStack.pop()
MyStack.pop()
MyStack.pop()
print(MyStack.pop())
print(MyStack.stacklist)
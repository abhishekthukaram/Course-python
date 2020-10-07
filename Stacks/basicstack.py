"""
Our goal will be to implement a Stack class that has the following behaviors:

push - adds an item to the top of the stack
pop - removes an item from the top of the stack (and returns the value of that item)
size - returns the size of the stack
top - returns the value of the item at the top of stack (without removing that item)
is_empty - returns True if the stack is empty and False otherwise
"""


class Stack:
    def __init__(self, initial_size=10):
        self.array = [None for i in range(initial_size)]
        self.next_index =0
        self.num_elements= 0

    def push(self,data):
        if self.next_index == len(self.array):
            print("Stack is full increasing capacity")
            self.is_stack_full()
        else:
            self.array[self.next_index] = data
            self.next_index+=1
            self.num_elements+=1

    def pop(self):
        self.next_index-=1
        self.num_elements-=1
        return self.array[self.next_index]

    def is_stack_full(self):
        old_array = self.array
        self.array = [None for i in range(2*len(self.array))]
        for index, element in enumerate(old_array):
            self.array[index] = element

    def sizeofstack(self):
        return self.num_elements

    def stack_isempty(self):
        if self.next_index == 0:
            return "Stack is empty"
        else:
            return "Stack is not empty"


simplestack = Stack()
#print (simplestack.sizeofstack())
#print (simplestack.stack_isempty())
simplestack.push(2)
simplestack.push(3)
simplestack.push(4)
simplestack.push(4)
simplestack.push(5)
simplestack.push(6)
simplestack.push(7)
simplestack.push(8)
print (simplestack.array)
print (simplestack.pop())
print (simplestack.pop())
print (simplestack.pop())
print (simplestack.pop())
#simplestack.push(9)
#simplestack.push(10)
#simplestack.push(11)
#print (simplestack.sizeofstack())
#print (simplestack.stack_isempty())
#print simplestack.array
#print (simplestack.pop())


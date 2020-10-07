"""
Problem Statement
Given an input string consisting of only { and }, figure out the minimum number of reversals required to make the
 brackets balanced.
For example:
For input_string = "}}}}, the number of reversals required is 2.
For input_string = "}{}}, the number of reversals required is 1.
If the brackets cannot be balanced, return -1 to indicate that it is not possible to balance them.
"""


class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


def minimum_bracket_reversals(input_string):
    """
    Calculate the number of reversals to fix the brackets

    Args:
       input_string(string): Strings to be used for bracket reversal calculation
    Returns:
       int: Number of bracket reversals needed
    """
    min = Stack()
    open_bracket  = 0
    closed_bracket = 0
    traversal =0
    if len(input_string) % 2 != 0:
        return -1
    for i in input_string:
        print i
        if i == "(" or i == "{" or i == '[':
            min.push(i)
            open_bracket+=1
            print min.top()
        else:
            if min.is_empty():
                min.push(i)
            elif i == "}" or i == ")" or i == ']':
                min.pop()
            closed_bracket+=1
            open_bracket-=1
    #print closed_bracket
    #print min.size()
    return (closed_bracket%2)+(open_bracket%2)


print minimum_bracket_reversals("}}}}")
#print minimum_bracket_reversals("}{{}")
#print minimum_bracket_reversals("{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}")
#print minimum_bracket_reversals("}}{}{}{}{}{}{}{}{}{}{}{}{}{}{}")

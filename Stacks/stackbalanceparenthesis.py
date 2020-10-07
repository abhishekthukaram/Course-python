"""
Balanced Parentheses Exercise
"""


class Stack:
    def __init__(self):
        self.stacklist = []

    def size(self):
        return len(self.stacklist)

    def push(self, item):
        self.stacklist.append(item)

    def pop(self):
        if len(self.stacklist)==0:
            return "Stack is empty"
        else:
            self.stacklist.pop()


def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """
    parenthesis = Stack()
    for i in equation:
        if i == "(" or i =="[" or i =="{":
            parenthesis.push(i)
        elif i == ")" or i=="]" or i == "}":
            parenthesis.pop()
    if parenthesis.size() != 0:
        return False
    return True
    # TODO: Intiate stack object

    # TODO: Interate through equation checking parentheses

    # TODO: Return True if balanced and False if not


print ("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
print ("Pass" if not (equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")
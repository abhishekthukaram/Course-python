"""
Add, Subtract, Multiply or Divide?
Write a function that takes two numbers and returns if they should be added, subtracted, multiplied or divided to get
24. If none of the operations can give 24, return None.
Examples
operation(15, 9) gives "added"
operation(26, 2) gives "subtracted"
operation(11, 11) gives None
"""


def operation(num1, num2):
    if num1+num2==24:
        return "added"
    elif num1-num2 ==24:
        return "subtracted"
    elif num1*num2 ==24:
        return 'multiplied'
    elif num1/num2 ==24:
        return 'divided'
    else:
        return None


print operation(15, 9)
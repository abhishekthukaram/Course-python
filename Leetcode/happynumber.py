"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by
the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy
numbers.
"""

def isHappy(n):
    remind = []
    sum_number = 0
    while n!=1:
        n = sum(int(x)**2 for x in str(n))
        if n in remind:
            return False
        else:
            remind.append(n)
    return True


print (isHappy(19))

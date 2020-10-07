"""
Write a function that reverses a string. The input string is given as an array of characters char[].
"""

def reversestring(s):
    left = 0
    right = len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left+1, right-1
    return s


print reversestring("hello")
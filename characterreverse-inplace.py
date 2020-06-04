"""
Write a function that takes a list of characters and reverses the letters in place.
"""


def reverse(list_of_chars):
    if len(list_of_chars) ==0:
        pass
    left = 0
    right = len(list_of_chars)-1
    temp = ""
    while left < right:
        temp = list_of_chars[left]
        list_of_chars[left] = list_of_chars[right]
        list_of_chars[right] = temp
        left+=1
        right-=1


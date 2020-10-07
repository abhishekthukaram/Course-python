"""
Given an unsorted list, create a function that returns the nth smallest element
(the smallest element is the first smallest, the second smallest element is the second smallest, etc).
nth_smallest([1, 3, 5, 7], 1) gives 1
nth_smallest([1, 3, 5, 7], 3) gives 5
nth_smallest([1, 3, 5, 7], 5) gives None
nth_smallest([7, 3, 5, 1], 2) gives 3
"""
"""
def smallest(lst):
    for i in range(len(lst)):
        minimim = i
        for j in range(i+1,len(lst)):
            if a[i
"""
def erase(string):
    new_str_list=[]
    for char in string:
        if char != "#":
            new_str_list.append(char)
        elif char == "#" and len(new_str_list) != 0:
            new_str_list.pop()
    return "".join(new_str_list)

print erase("#Abhi#shek")
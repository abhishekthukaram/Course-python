"""
Find the Index (Part 1)
Create a function that finds the index of a given item.
Examples
search([1, 5, 3], 5) gives 1
search([9, 8, 3], 3) gives 2
search([1, 2, 3], 4) gives -1
"""


def search(lst, item):
    for index, value in enumerate(lst):
        if value == item:
            return index
    return -1


print search([1, 5, 3], 5)
print search([9, 8, 3], 3)
print search([1, 2, 3], 4)

"""
Find the Index (Part 2)
Create a function that finds the index of a given item if the list is sorted.
Examples
search([1, 2, 3, 4], 3) gives 2
search([2, 4, 6, 8, 10], 8) gives 3
search([1, 3, 5, 7, 9], 11) gives -1
"""


def search(lst, item):
    if lst == sorted(lst):
        for index, value in enumerate(lst):
            if value == item:
                return index
    return -1


print search([1, 2, 3, 4], 3)
print search([2, 4, 6, 8, 10], 8)
print search([1, 3, 5, 7, 9], 11)
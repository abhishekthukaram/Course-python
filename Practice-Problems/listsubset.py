"""
Check if One List is Subset of Another.List A is contained inside list B if each element in A also exists in B.
The number of times a number is present doesn't matter. In other words, if we transformed both lists into sets,
A would be a subset of B.
"""


def subset(lst1, lst2):
    for i in lst1:
        if i not in lst2:
            return False
    return True

print subset([1, 3], [1, 3, 3, 5])


def largest_swap(num):
    first_digit = num // 10
    second_digit = num % 10
    swap_digit = second_digit * 10 + first_digit
    if swap_digit > num:
        return True
    return False

"""
Minimum Removals to Make Sum Even
Create a function that returns the minimum number of elements removed to make the sum of all elements in a list even.
minimum_removals([1, 2, 3, 4, 5]) give 1
minimum_removals([5, 7, 9, 11]) give 0
minimum_removals([5, 7, 9, 12]) give 1
"""


def minimum_removals(lst):
    count_odd = 0
    for i in lst:
        if i%2 != 0:
            count_odd += 1
    if count_odd%2 == 0:
        return 0
    return 1


print (minimum_removals([1, 2, 3, 4, 5]))
print (minimum_removals([5, 7, 9, 11]))
print(minimum_removals([5, 7, 9, 12]))
"""
Create a function that returns True an input array can be completely sorted by only sorting within the bounds [0, n]
(inclusive), where n smaller than or equal to the array's length, and False otherwise.
bound_sort([1, 6, 5, 3, 8, 9], [0, 3]) will give  True
# If [1, 6, 5, 3] is sorted to [1, 3, 5, 6], the array is completely sorted.
bound_sort([1, 6, 5, 3, 8, 9], [0, 2]) will give False
# Even if [1, 6, 5] is sorted to [1, 5, 6], the array is still not completely sorted.
bound_sort([1, 9, 2, 5, 7], [0, 4]) will give True
bound_sort([1, 9, 2, 5, 7], [0, 3]) will give False
# Sorting from [0, 3] gives us [1, 2, 5, 9, 7],
"""

def bound_sort(lst, bounds):
    if bounds[1] > len(lst):
        return True






def bound_sort(lst):
    lst.sort()
    print lst



print bound_sort([1, 6, 5, 3, 8, 9])
#print bound_sort([1, 9, 2, 5, 7], [0, 4])
#print bound_sort([1, 9, 2, 5, 7], [0, 3])

"""

def bound_sort(lst, bounds):
    h_bound = bounds[1]
    if h_bound >= len(lst):
        return True
    max = lst[0]
    for i in range(h_bound+1):
        if lst[i] > max:
            max = lst[i]
    print lst
    for j in range(h_bound+1, len(lst)):
        if lst[j] < max:
            return False
            max = lst[j]

    return True
"""
#print bound_sort([1, 6, 5, 3, 8, 9], [0, 3])
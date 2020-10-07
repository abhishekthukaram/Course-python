"""
[(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
[(0, 1), (3, 8), (9, 12)]
"""
def merge_list(lst):
    merge1 = sorted(x[0] for x in lst)
    merge2 = sorted(y[1] for y in lst)
    print merge1, merge2
merge_list([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])



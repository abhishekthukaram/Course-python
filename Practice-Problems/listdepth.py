def depth(lst):
    count = str(lst)
    print count
    counter =0
    for i in count:
        if i == '[':
            counter+=1
    return counter


print depth([1, 2, 3, 4])
print depth([1, [2, 3, 4]])
print depth([1, [2, [3, 4]]])
print depth([1, [2, [3, [4]]]])
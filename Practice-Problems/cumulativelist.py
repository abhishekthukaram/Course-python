def cumulative_sum(list1):
    for i in range(1, len(list1)):
        list1[i] = list1[i] + list1[i - 1]
    return list1

print add_one_by_one([1, 3, 6])
print add_one_by_one([1, -1, 2])


def cumulativelist(list1):
    new = []
    cum = 0
    for i in list1:
        cum += i
        new.append(cum)
    return new
def sorttuple(tup):
    new_tup= list(tup)
    if len(tup)>1:
        mid =  len(tup)//2
        lefthalf = list(tup[:mid])
        righthalf = list(tup[mid:])
        print lefthalf
        print righthalf

        sorttuple(lefthalf)
        sorttuple(righthalf)
        i=0
        j=0
        k=0
        while i<len(lefthalf) and j< len(righthalf):
            if lefthalf[i] < righthalf[j]:
                new_tup[k] = lefthalf[i]
                i=i+1
                k=k+1
            else:
                new_tup[k]=righthalf[j]
                j=j+1
                k=k+1
        while i < len(lefthalf):
            new_tup[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            new_tup[k] = righthalf[j]
            j += 1
            k += 1
    #print new_tup


while i < len(lefthalf):
    tup[k] = lefthalf[i]
    i += 1
    k += 1

while j < len(righthalf):
    tup[k] = righthalf[j]
    j += 1
    k += 1

def getKey(item):
    return item[0]


def getfirst(item):
    return item[0]
"""

def selectionsort(sortlist):
    for i in range(len(sortlist)):
        minimum = sortlist[i][1]
        for j in range(i+1, (len(sortlist))):
            if sortlist[minimum]>sortlist[j][1]:
                minimum = sortlist[j][1]
                print sortlist[j][1]
        temp = sortlist[i]
        sortlist[i] = sortlist[minimum]
        sortlist[minimum]=temp
    return sortlist


print selectionsort(((3, 3), (1, 5), (2, 5), (1, 2), (2, 3), (1, 7), (3, 2), (2, 2)))

def tuplesort(tup):
    for i in range(len(tup)):


def tuplesort(tup):
    #neww = sorted(tup, key=getKey)
    neww= sorted(tup, key=lambda tup: (tup[0], tup[1]))
    print neww

"""
tuplesort(((3, 3), (1, 5), (2, 5), (1, 2), (2, 3), (1, 7), (3, 2), (2, 2)))
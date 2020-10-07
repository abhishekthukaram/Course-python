"""
def merge_arrays(a, b):
    result = [0]*(len(a)+len(b))
    i=0
    j=0
    k=0
    while i < len(a) and j < len(b):
        result[k]= a[i]
        k+=1
        i+=1
        result[k]=b[j]
        k+=1
        j+=1
    while i <len(a):
        result[k]= a[i]
        i+=1
        k+=1
    while j<len(b):
        result[k]=b[j]
        j+=1
        k+=1
    return result
"""

#print (merge_arrays(["a", "b", "c"], [1, 2, 3, 4,5]))


def merge_arrays(a, b):
    result = min(len(a),len(b))
    output = []
    for i in range(result):
        output.append(a[i])
        output.append(b[i])
    if len(a) > len(b):
        output.extend(a[result:len(a)])
    else:
        output.extend(b[result:len(b)])
    return output


print (merge_arrays(["a", "b", "c"], [1, 2, 3, 4,5]))
"""
Write a function that returns the smallest N-digit number which is a multiple of the specified value.
Examples
smallest(3, 8) gives 104
# Smallest 3 digit integer that is a multiple of 8
smallest(5, 12) gives 10008
smallest(7, 1) gives 1000000
smallest(2, 3) gives 12
"""
def smallest(digits, value):
    n =0
    result =0
    while True:
        result = value*n
        n+=1
        if len(str(result))==digits:
            break
    return result


print (smallest(3,8))
print (smallest(7, 1))
print (smallest(2, 3))
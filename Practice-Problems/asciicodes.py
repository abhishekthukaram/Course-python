"""
Compare by ASCII Codes
Create a function to that compares two words based on the sum of their ASCII codes and returns the word
with the smaller ASCII sum.

Examples
ascii_sort(["hey", "man"]), "man"
["h", "e", "y"],sum([104, 101, 121]),326
["m", "a", "n"] ,sum([109, 97, 110]),316
ascii_sort(["majorly", "then"]),"then"
ascii_sort(["victory", "careless"]) ,"victory"
"""


def calculateascii(string1):
    sum =0
    str_list =  list(string1)
    for i in  str_list:
        sum+=ord(i)
    return sum


def ascii_sort(lst):
    sum_ascii0 = calculateascii(lst[0])
    sum_ascii1 = calculateascii(lst[1])
    if sum_ascii0>sum_ascii1:
        return lst[1]
    else:
        return lst[0]


print(ascii_sort(["hey", "man"]))
print (ascii_sort(["majorly", "then"]))
print(ascii_sort(["victory", "careless"]))
#print calculateascii("hey")




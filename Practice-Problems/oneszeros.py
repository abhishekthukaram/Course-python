"""
Write a function that returns True if every consecutive sequence of ones is followed by a consecutive sequence
of zeroes of the same length.
same_length("110011100010") gives True
same_length("101010110") gives False
same_length("111100001100") gives True
same_length("111") gives False
"""

def same_length(txt):
    count_0,count_1 =0, 0
    for i, char in enumerate(txt):
        if int(txt[i-1]) - int(txt[i]) == 0 and int(txt[i]) == 1:
            count_1+=1
        elif int(txt[i-1])-int(txt[i])==0:
            count_0+=1
        if count_0 == count_1 and i == len(txt)-1:
            return True
    return False


print same_length("110011100010")
print same_length("101010110")
print same_length("111100001100")
print same_length("101")
print same_length("111")


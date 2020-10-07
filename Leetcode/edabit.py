"""
def list_of_multiples (num, length):
    result = []
    for i in range(1, length+1):
        output = num*i
        #print (output)
        result.append(output)
    return result


print (list_of_multiples(7,5))


def length(txt):
    if txt == "":
        return 0
    else:
        output = 1 +length(txt[1::])
    return output


print length("apple")


def sum_numbers(n):
    out_sum = 1
    if n == 1:
        return out_sum
    else:
        output = n + sum_numbers(n-1)
        return output


print sum_numbers(5)


def UpDown(str):
    swap = list(str)
    result = ""
    if str == "":
        return ""
    else:
        for i in str:
            if i.islower():
                result+=i.upper()
            else:
                result+=i.lower()
    return result


print (UpDown("HELLO"))

def abcmath(a, b, c):
    sum_a = 0
    i = 0
    while i<=b:
        if i ==0:
            sum_a+=a
        else:
            sum_a+=sum_a
        print sum_a
        i+=1
    print sum_a
    return sum_a%c ==0


print (abcmath(42,5,10))

"""


def double_letters(word):
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            return True
    return False


print double_letters("yumy")

#list to integers and vice versa


def to_list(num):
    return [int(i) for i in str(num)]


def to_number(lst):
    out = [str(x) for x in lst]
    return int("".join(out))



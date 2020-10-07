from itertools import permutations
"""
Create a function that takes in a list of integers and returns the integers that are either palindromes or
almost-palindromes. An almost-palindrome is any integer that can be rearranged to form a palindrome.
For example, the numbers 677 and 338 are both almost-palindromes, since they can be rearranged to form 767 and 383,
respectively.
"""
"""

def checkpallindrome(number):
    original = str(number)
    reverse = original[::-1]
    if original == reverse:
        return number


def rearrange(number_find):
    check = 0
    if len(str(number_find)) ==1:
        return number_find
    rearrange_list = []
    string_rearrange= list(str(number_find))
    length = len(str(number_find))
    number = permutations(string_rearrange, length)
    for i in set(number):
        result = int("".join(i))
        rearrange_list.append(result)
    for i in rearrange_list:
        if checkpallindrome(i):
            check+=1
    if check>0:
        return number_find


def palindrome_sieve(nums):
    output_list = []
    for i in nums:
        pal=rearrange(i)
        if pal:
            output_list.append(i)
    return output_list
    
"""

def palindrome_sieve(alist):
    unpaired_chars = set()
    pali = []
    for word in alist:
        #print word
        for ch in str(word):
            #print ch
            if ch in unpaired_chars:
                unpaired_chars.remove(ch)
            else:
                unpaired_chars.add(ch)
        #print(unpaired_chars)
        if len(unpaired_chars) <= 1:
            pali.append(int(word))
        unpaired_chars.clear()
    return pali


print palindrome_sieve([443, 12, 639, 121, 3232])
print palindrome_sieve([5, 55, 6655, 8787])
print palindrome_sieve([897, 89, 23, 54, 6197, 53342])

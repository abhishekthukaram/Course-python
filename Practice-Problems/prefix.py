def longest_match(str1):
    for i in range(len(str1)):
        if len(str1)%2 == 0:
            prefix = str1[:len(str1)//2 - i]
            suffix = str1[len(str1)//2 - i:]
        elif len(str1)%2 != 0:
            prefix = str1[:len(str1)//2 - i]
            suffix = str1[((len(str1)//2)+ 1) - i:]
        if prefix == suffix:
            return prefix,len(prefix)
    return ""

print(longest_match("aabcdaabc"))
print(longest_match("abcab"))
print(longest_match("aaaa"))
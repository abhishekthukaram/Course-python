"""
Given two strings s and t , write a function to determine if t is an anagram of s.
"""

'''Method1'''


def checkAnagram(s, t):
    return sorted(s) == sorted(t)


print checkAnagram("anagram","nagaram")


'''Method2'''


def isAnagram(s, t):
    dict1_s = {}
    result = []
    if len(s)!= len(t):
        return False
    for i in s:
        if i in dict1_s:
            dict1_s[i]+=1
        else:
            dict1_s[i]=1
    for j in t:
        if j in dict1_s:
            dict1_s[j]-=1
            result.append(j)
    if len(s) != len(result):
        return False
    else:
        return True


print isAnagram("anagram","nagaram")
print isAnagram('rat','car')

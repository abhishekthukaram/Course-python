"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of
same characters.
"""

def palindromesubstring(s):
    N = len(s)
    output = 0
    for center in range(2*N-1):
        left = center/2
        right = left+center%2
        while left>=0 and right < N and s[left] == s[right]:
            output+=1
            left-=1
            right+=1
    return output


print palindromesubstring("aaa")
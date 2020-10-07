"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
"""


def longestPalindrome(s):
    result = ""
    if len(s) ==1:
        result+=s
    elif len(s) ==2:
        if s == s[::-1]:
            result+=s
        return result
    for i in range(len(s)+1):
        for j in range(i, len(s)+1):
            print s[i:j]
            if s[i:j] == (s[i:j][::-1]) and len(s[i:j])>len(result):
                result = s[i:j]
    return result


print longestPalindrome("c")
"""
Given two strings s and t, determine if they are both one edit distance apart.
Note:
There are 3 possiblities to satisify one edit distance apart:
Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
"""
def editstring(s,t):
    max_length = max(len(s), len(t))
    diff = 0
    for i in range(max_length):
        if max_length == len(s):
            if s[i] not in t:
                diff+=1
        elif max_length == len(t):
            if t[i] not in s:
                diff+=1
        else:
            if s[i] not in t[i]:
                diff+=1
    if diff ==1:
        return True

elif max_length == len(t):
if s[i] != t[i]:
    print("Entered")
    print("This is t", t[i + 1:])
    print("This is s", s[i:])
    return t[i + 1:] == s[i:] or len(s) + 1 == len(t)
elif len(s) or len(t) == 0:
    return True
print editstring(s="a", t="A")






class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        diff = 0
        if abs(len(s)-len(t)) >1:
            print("Entered")
            return False
        if len(s)==len(t):
            for i in range(len(s)):
                if s[i] != t[i]:
                    diff+=1
            return diff == 1

        if len(s) > len(t):

            for i in range(len(s)):
                if s[i] != t[i]:
                    return s[i+1:] == t[i:]
            return True
        else:
            for i in range(len(t)):
                if t[i] != s[i]:
                    return t[i+1:] == s[i:]
            return True

    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        Sn = len(s)
        Tn = len(t)
        diff = 0
        if abs(len(s) - len(t)) > 1:
            return False
        if len(s) > len(t):
            s, t = t, s
            Sn, Tn = Tn, Sn
        for i in range(Sn):
            if s[i] != t[i]:
                if Sn == Tn:
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i:] == t[i + 1:]
        return Sn + 1 == Tn
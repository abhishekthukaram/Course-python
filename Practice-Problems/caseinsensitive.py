"""
Case Insensitive Comparison
Write a function that validates whether two strings are identical. Make this validator case insensitive.
"""


def match(s1, s2):
    if len(s1)!=len(s2):
        return False
    else:
        for i in range(len(s1)):
            if s1[i].lower() != s2[i].lower():
                return False
    return True


print match("EXCEl", "exceLs")
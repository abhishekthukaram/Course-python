"""
Filter Repeating Character Strings
Create a function that keeps only strings with repeating identical characters (in other words, it has a set size of 1).
identical_filter(["aaaaaa", "bc", "d", "eeee", "xyz"]) gives ["aaaaaa", "d", "eeee"]
identical_filter(["88", "999", "22", "545", "133"]) gives ["88", "999", "22"]
identical_filter(["xxxxo", "oxo", "xox", "ooxxoo", "oxo"]) gives  []
"""


def identical_filter(lst):
    output_list=[]
    for value in lst:
        filter= check_character(value)
        if filter:
            output_list.append(filter)
    return output_list


def check_character(s):
    for i in range(len(s)):
        if s[i]!=s[0]:
            return None
    return s


print identical_filter(["aaaaaa", "bc", "d", "eeee", "xyz"])
print (identical_filter(["88", "999", "22", "545", "133"]))
print (identical_filter(["xxxxo", "oxo", "xox", "ooxxoo", "oxo"]))


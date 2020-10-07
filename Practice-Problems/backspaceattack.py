"""
Suppose a hash # represents the backspace key being pressed. Write a function that transforms a string containing #
into a string without any #.
erase("he##l#hel#llo") gives "hello"
erase("major# spar##ks") gives "majo spks"
erase("si###t boy") gives "t boy"
erase("####") gives ""
"""

def erase(txt):
    new_string =[]
    for character in txt:
        if character=='#'and len(new_string)>=1:
            new_string.pop()
        elif character=='#' and len(new_string)==0:
            pass
        else:
            new_string.append(character)
    string = "".join(new_string)
    return string


print erase("he##l#hel#llo")
print erase("#t boy")
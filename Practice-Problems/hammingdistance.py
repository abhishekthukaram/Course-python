"""
Hamming distance is the number of characters that differ between two strings.

String1: "abcbba"
String2: "abcbda"

Hamming Distance: 1 - "b" vs. "d" is the only difference.
"""
"""

def hamming_distance(txt1, txt2):
    count =0
    zipped = zip(txt1,txt2)
    for char1, char2 in zipped:
        if char1!=char2:
            count+=1
    return count
"""


def repeat(txt, n):
    for i in txt:
        char = i*n
        print char
        output = "".join(char)
        print output
    return output

print(repeat("hello", 3))
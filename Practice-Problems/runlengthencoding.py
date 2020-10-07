"""
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent
repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA"
would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists
solely of alphabetic characters. You can assume the string to be decoded is valid
"""


def characterencoding(input_string):
    count=1
    i =0
    output_string= ""
    character = input_string[0]
    for i in range(1,len(input_string)):
        if input_string[i]==character:
            count+=1
        else:
            output_string+=str(count)+character
            count = 1
            character= input_string[i]
    output_string += str(count) + character
    return output_string


print (characterencoding("AAAABBBCCDAA"))




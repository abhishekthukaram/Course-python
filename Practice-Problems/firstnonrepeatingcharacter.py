"""
Create a function that accepts a string as an argument and returns the first non-repeated character.
Examples
first_non_repeated_character("it was then the frothy word met the round night")  "a"
first_non_repeated_character("the quick brown fox jumps then quickly blows air") "f"
first_non_repeated_character("g")  "g"
first_non_repeated_character("") False
first_non_repeated_character("hheelloo")False
Notes
An empty string should return False.
If every character repeats, return False.
Don't worry about case sensitivity or non-alphanumeric characters.
"""
"""
def checknonrepeating(str):
    counter = {}
    charcter = []
    for c in str:
        if c in charcter:
            counter[c] += 1
        else:
            counter[c] = 1
            charcter.append(c)
    print counter
    print charcter
    for i in charcter:
        if counter[i] == 1:
            return i
    return False
"""
def check_non_repeating1(string):
    char_dict = {}
    for char in string:
        char_dict[char] += 1
    print(char_dict)
    for i, char in enumerate(string):
        if char_dict[char] == 1:
            return char
    return False


def check_non_repeating(string):
    char_dict = {}
    for char in string:
        if char in char_dict:
            char_dict[char] += 1
        elif char not in char_dict:
            char_dict[char] = 1
    print char_dict
    for i, char in enumerate(string):
        print i,char
        if char_dict[char] == 1:
            return char
    return False

print check_non_repeating("hheelloo")
print check_non_repeating("it was then the frothy word met the round night")

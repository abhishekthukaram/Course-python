"""
A palindrome is a word, phrase, number or other sequence of characters which reads the same backward or forward,
such as madam or kayak.Write a function that takes a string and determines whether it's a palindrome or not.
The function should return a boolean (True or False value).
is_palindrome("A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal-Panama!") gives True
is_palindrome("Neuquen") gives True
is_palindrome("Not a palindrome") gives False
"""
import string


def remove_punctuation(input_string):
    result = ""
    for char in input_string:
        if char not in string.punctuation:
            result+=char
    return result


def is_palindrome(txt):
    txt_string= txt.lower().replace(" ", "")
    pal_string = remove_punctuation(txt_string)
    return pal_string[::] == pal_string[::-1]


print is_palindrome("A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal-Panama!")
print is_palindrome("Neuquen")
print is_palindrome("Not a palindrome")

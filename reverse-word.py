"""
Write a function reverse_words() that takes a message as a list of characters and
reverses the order of the words in place
"""


def reverse_characters(message, left, right):
    while left < right:
        message[left], message[right] = message[right], message[left]
        left += 1
        right -= 1


def reverse_words(message):
    reverse_characters(message, 0, len(message) - 1)
    print(message)
    current_start = 0
    for i in range(len(message) + 1):
        print(len(message))
        if (i == len(message)) or (message[i] == ' '):
            reverse_characters(message, current_start, i - 1)
            current_start = i + 1
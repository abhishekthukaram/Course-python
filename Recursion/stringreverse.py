"""
Reverse a string using recursion
"""

def reverse_string(input):
    """
    Return reversed input string

    Examples:
       reverse_string("abc") returns "cba"

    Args:
      input(str): string to be reversed

    Returns:
      a string that is the reverse of input
    """
    if input=="":
        return input
    else:
        print input[1:]
        return reverse_string(input[1:])+input[0]


print reverse_string('abc')


def is_palindrome(input):
    """
    Return True if input is palindrome, False otherwise.

    Args:
       input(str): input to be checked if it is palindrome
    """
    if len(input)<=1:
        return True
    else:
        first = input[0]
        last = input[-1]
        return first == last and is_palindrome(input[1:-1])


print is_palindrome('madame')

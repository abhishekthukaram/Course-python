"""
Write an efficient function that checks whether any permutation ↴ of an input string is a palindrome. ↴
"""

def has_palindrome_permutation(the_string):
    result = {}
    count = 0
    final_result = 0
    if (len(the_string) == 0):
        return True
    for key in the_string:
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    for sum_value in result.keys():
        if result[sum_value] == 1:
            final_result += 1
    if len(the_string) % 2 == 0:
        if final_result == 0:
            return True
    else:
        if final_result == 1:
            return True
    return False


print(has_palindrome_permutation("civic"))


"""
def has_palindrome_permutation(the_string):
    # Track characters we've seen an odd number of times
    unpaired_characters = set()

    for char in the_string:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)

    # The string has a palindrome permutation if it
    # has one or zero characters without a pair
    return len(unpaired_characters) <= 1
"""

"""
Create a function that counts the number of times a particular letter shows up in the word search.
letter_counter([
  ["D", "E", "Y", "H", "A", "D"],
  ["C", "B", "Z", "Y", "J", "K"],
  ["D", "B", "C", "A", "M", "N"],
  ["F", "G", "G", "R", "S", "R"],
  ["V", "X", "H", "A", "S", "S"]
], "D") gives 3
letter_counter([
  ["D", "E", "Y", "H", "A", "D"],
  ["C", "B", "Z", "Y", "J", "K"],
  ["D", "B", "C", "A", "M", "N"],
  ["F", "G", "G", "R", "S", "R"],
  ["V", "X", "H", "A", "S", "S"]
], "H") gives 2


def letter_counter(lst, letter):
    letter_count = 0
    for list_num in lst:
        for char in list_num:
            if char == letter:
                letter_count+=1
    return letter_count

"""


def remove_nested(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result.extend(remove_nested(i))
        else:
            result.append(i)
    return result


def letter_count(lst, letter):
    count = 0
    output = remove_nested(lst)
    for char in output:
        if char == letter:
            count+=1
    return count

"""
#print letter_counter([
  ["D", "E", "Y", "H", "A", "D"],
  ["C", "B", "Z", "Y", "J", "K"],
  ["D", "B", "C", "A", "M", "N"],
  ["F", "G", "G", "R", "S", "R"],
  ["V", "X", "H", "A", "S", "S"]
], "D")
"""

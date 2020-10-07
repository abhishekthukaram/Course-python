"""
Create a function that takes an initial word and filters out a list to contain words that start with the same
letters as the initial word.
dictionary("tri", ["triplet", "tries", "trip", "piano", "tree"]) should give  ["triplet", "tries", trip"]
dictionary("bu", ["button", "breakfast", "border"]) should give ["button"]
dictionary("beau", ["pastry", "delicious", "name", "boring"]) should give  []
"""


def dictionary(initial, words):
    newlist = []
    for i in words:
        if initial in i:
            newlist.append(i)
    return newlist


print(dictionary("tri", ["triplet", "tries", "trip", "piano", "tree"]))
print (dictionary("bu", ["button", "breakfast", "border"]))
print(dictionary("beau", ["pastry", "delicious", "name", "boring"]))
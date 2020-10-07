"""
Given an array of strings, group anagrams together.
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""


def groupAnagrams(input_list):
    result = {}
    output = []
    for i in input_list:
        validate_string = tuple(sorted(i))
        print(validate_string)
        if validate_string in result.keys():
            result[validate_string].append(i)
            print(result)
        else:
            result[validate_string] = [i]
    for value in result.keys():
        output.append(result[value])
    return output


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
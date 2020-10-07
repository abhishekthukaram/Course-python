"""
Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""


def lengthoflongestsubstring(s):
    long_str = ""
    length = 0
    for i in s:
        if i in long_str:
            long_str = long_str[long_str.index(i) + 1:]
        long_str+=i
        length = max(length, len(long_str))
    return length


print lengthoflongestsubstring("abcabcbb")
print len(set("abcabcbb"))


def lengthofstring(s):
    result = []
    length = 0
    for character in s:
        print character
        if character not in result:
            result.append(character)
        else:
            result.remove(character)
    print result
    output= "".join(result)
    return len(output)

print lengthofstring("abcabcbb")

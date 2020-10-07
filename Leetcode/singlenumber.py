"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
"""


def singlenumber(num_list):
    result = {}
    for i in num_list:
        if i in result:
            result[i] +=1
            print result
        else:
            result[i] = 1
    for key, value in result.items():
        if value == 1:
            return key


print singlenumber([4,1,2,1,2])
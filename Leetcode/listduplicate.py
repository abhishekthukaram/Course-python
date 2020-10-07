"""
Contains Duplicate
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if
every element is distinct.
Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
def checkduplicate(input_list):
    result= {}
    for i in range(len(input_list)):
        if input_list[i] in result:
            result[input_list[i]]+=1
        else:
            result[input_list[i]] = 1
    for value in result:
        if result[value] !=1:
            return True
    return False


print checkduplicate([1,2,3,4])
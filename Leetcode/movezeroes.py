"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the
non-zero elements.
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
"""


def movezeroes(numbers_list):
    for i in range(len(numbers_list)):
        for j in range(i+1,len(numbers_list)):
            if numbers_list[i] and numbers_list[j] ==0:
                pass
            elif numbers_list[i] ==0:
                temp = numbers_list[i]
                numbers_list[i] = numbers_list[j]
                numbers_list[j] = temp
    return numbers_list


print movezeroes([0,1,0,3,12])
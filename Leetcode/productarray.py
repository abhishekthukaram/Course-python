"""
Product of Array Except Self
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of
all the elements of nums except nums[i]
Input:  [1,2,3,4]
Output: [24,12,8,6]
"""


def productexceptself(nums):
    L = len(nums)
    left_array= [0]* L
    right_array = [0]*L
    left_array[0]= 1
    right_array[L-1] = 1
    answer = [0]*L
    for i in range(1, len(nums)):
        left_array[i] = left_array[i-1] * nums[i-1]
    for i in reversed(range(len(nums)-1)):
        print i
        right_array[i] = right_array[i+1]*nums[i+1]
    for i in range(len(nums)):
        answer[i] = left_array[i] * right_array[i]
    return answer


print productexceptself([1,2,3,4])
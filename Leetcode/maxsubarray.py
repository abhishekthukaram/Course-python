"""
Maximum Product Subarray
Given an integer array nums, find the contiguous subarray within an array (containing at least one number)
which has the largest product.
Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

def maxproduct(input_list):
    product = 0
    if len(input_list)==1:
        return input_list[0]
    for i in range(len(input_list)-1):
        if input_list[i]*input_list[i+1]> product:
            product = input_list[i] * input_list[i+1]
    return product


print maxproduct([2,3,-2,4])
print maxproduct([0,2])
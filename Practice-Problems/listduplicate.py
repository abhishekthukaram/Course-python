"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return
the new length.
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.
"""

def removeDuplicates(nums):
    compare_index = 0
    for i in range(1,len(nums)):
        if nums[i] != nums[compare_index]:
            compare_index+=1
            nums[compare_index] = nums[i]
    return compare_index+1

print removeDuplicates([1,1,2])
print removeDuplicates([0,0,1,1,1,2,2,3,3,4])
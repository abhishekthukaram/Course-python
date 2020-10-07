def twosum(nums, target):
    result = {}
    for pos, num in enumerate(nums):
        remaining = target-num
        if remaining in result:
            return [result[remaining], pos]
        else:
            result[num] = pos
    return []


print (twosum([2,7,9,11], 9))
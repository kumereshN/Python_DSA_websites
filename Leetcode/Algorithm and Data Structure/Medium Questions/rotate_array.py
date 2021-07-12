def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    k %= len(nums)
    nums[k:], nums[:k] = nums[:-k], nums[-k:]


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)


"""
Swap first half with the last half:
nums[:k] = nums[-k:]
[1,2,3] = [5,6,7]

Result = [5,6,7,4,1,2,3]

Swap last half with the first half,
nums[k:] = nums[:-k]
[4,1,2,3] = [5,6,7,4]

Result = [5,6,7,1,2,3,4]
"""

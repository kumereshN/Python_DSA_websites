def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    k %= len(nums)
    nums[k:], nums[:k] = nums[:-k], nums[-k:]

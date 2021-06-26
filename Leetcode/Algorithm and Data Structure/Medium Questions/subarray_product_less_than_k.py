def numSubarrayProductLessThanK(nums, k):
    if k <= 1: return 0 #
    prod = 1
    ans = left = 0
    for right, val in enumerate(nums):
        prod *= val
        while prod >= k: # When the product is more than or equal to k
            prod /= nums[left] # Divide product by the nums[left]
            left += 1 # Increment left by 1
        ans += right - left + 1 # get the difference between (right and left) + 1
    return ans

nums = [10, 5, 2, 6]
k = 100
numSubarrayProductLessThanK(nums,k)

"""
while prod >= k:
If the product is equal to or greater than k, the prod gets divided by the left index.
E.g: 100/10 = 10, which is the first index
Then, increment left by 1.
[5,2,6] == [5] * [2] * [6] == 60, so a total of 3 elements added to ans.
"""

def subarray_sum_divisible(nums, k):
    """ Brute force solution """
    left, right = 0, 0
    count = 0
    n = len(nums)

    while left < n:
        while right < n:
            total_sum = sum(nums[left:right+1])
            if total_sum % k == 0:
                count += 1
            right += 1
        right = left + 1
        left = right
    return count


nums = [3, 1, 2, 5, 1]
k = 3
subarray_sum_divisible(nums, k)

from typing import List
from collections import Counter

def subarray_sum_divisible(nums: List[int], k: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    count = 0
    remainders = Counter({0:1})
    cur_sum = 0
    n = len(nums)
    
    for i in range(n):
        num = nums[i]
        cur_sum += num
        remainder = cur_sum % k
        if remainder in remainders:
            count += remainders[remainder]
        remainders[remainder] += 1
    return count

nums = [3, 1, 2, 5, 1]
k = 3
subarray_sum_divisible(nums, k)
# My Answer
def subarray_sum(arr, target):
    left, right = 0, 0
    total_sum = 0
    n = len(arr)

    while left < n:
        while right < n:
            right += 1
            total_sum = sum(arr[left:right+1])
            if total_sum == target:
                return [left, right+1]
        right = left + 1
        left = right


arr = [1, -20, -3, 30, 5, 7]
target = 7

subarray_sum(arr, target)


from typing import List

def subarray_sum(arr: List[int], target: int) -> List[int]:
    """ Official solution """
    # prefix_sum 0 happens when we have an empty array
    prefix_sums = {0: 0}
    cur_sum = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        complement = cur_sum - target
        if complement in prefix_sums:
            return [prefix_sums[complement], i + 1]
        prefix_sums[cur_sum] = i + 1

from typing import List
from collections import Counter

def subarray_sum_total(arr: List[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    """ Official solution to count the number of subarrays """
    prefix_sum = Counter()
    prefix_sum[0] = 1 # since empty array's sum is 0
    count = cur_sum = 0
    
    for i in range(len(arr)):
        cur_sum += arr[i]
        complement = cur_sum - target
        if complement in prefix_sum:
            count += prefix_sum[complement]
        prefix_sum[cur_sum] += 1
    return count
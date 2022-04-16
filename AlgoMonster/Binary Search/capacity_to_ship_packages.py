from typing import List

from typing import List

def min_max_weight(weights: List[int], d: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    """
    Optimum solution
    source: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/discuss/256729/JavaC%2B%2BPython-Binary-Search
    """
    left, right = max(weights), sum(weights)
    while left < right:
        mid, need, cur = (left + right) // 2, 1, 0
        for w in weights:
            if cur + w > mid:
                need += 1
                cur = 0
            cur += w
        if need > d:
            left = mid + 1
        else:
            right = mid
    return left

def feasible(weights: List[int], max_weight: int, req_days: int) -> int:
    """
    Algomonster solution
    """
    total_days = 1
    # max_weight is minimum capacity we want
    capacity = max_weight
    i = 0
    n = len(weights)
    while i < n:
        if weights[i] <= capacity:
            capacity -= weights[i]
            i += 1
        else:
            # If we've reached the max capacity, increment total_days by 1
            # Reset the capacity
            total_days += 1
            capacity = max_weight
    return total_days <= req_days

def min_max_weight(weights: List[int], d: int) -> bool:
    min_ptr = max(weights)
    max_ptr = sum(weights)
    boundary_index = max_ptr
    while min_ptr <= max_ptr:
        midpoint = (min_ptr + max_ptr) // 2
        if feasible(weights, midpoint, d):
            boundary_index = midpoint
            max_ptr = midpoint - 1
        else:
            min_ptr = midpoint + 1
    return boundary_index
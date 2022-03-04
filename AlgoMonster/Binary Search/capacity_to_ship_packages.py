from typing import List

def feasible(weights: List[int], max_weight: int, d: int) -> int:
    req_days = 1
    capacity = max_weight
    i = 0
    n = len(weights)
    while i < n:
        if weights[i] <= capacity:
            capacity -= weights[i]
            i += 1
        else:
            # If we've reached the max capacity, increment req_days by 1
            # Reset the capacity
            req_days += 1
            capacity = max_weight
    return req_days <= d

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
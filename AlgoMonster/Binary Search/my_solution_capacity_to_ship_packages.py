from typing import List

def feasible(weights, minimum_capacity, required_days):
    """ 
    Does not work
    """
    i = 0
    n = len(weights)
    total_weight = 0
    total_days = 1

    while i < n:
        total_weight += weights[i]
        i += 1
        if total_weight >= minimum_capacity:
            total_days += 1
            total_weight = 0
            i -= 1   
    return total_days <= required_days

def min_max_weight(weights: List[int], d: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    min_ptr = max(weights)
    max_ptr = sum(weights)
    boundary_index = max_ptr

    while min_ptr <= max_ptr:
        midpoint = (min_ptr + max_ptr) // 2
        # if it's feasible: the middle weight is less than or equal to the required days
        if feasible(weights, midpoint, d):
            boundary_index = midpoint
            max_ptr = midpoint - 1
        else:
            min_ptr = midpoint + 1
    return boundary_index 

# weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
weights = [1,2,3,1,1]
days_to_ship = 4
print(min_max_weight(weights, days_to_ship))
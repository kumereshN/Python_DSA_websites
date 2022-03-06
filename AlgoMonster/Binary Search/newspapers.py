from typing import List

def feasible(newspapers: List[int], init_time: int, coworkers: int) -> bool:
    """ Same as capacity to ship packages problem """
    i = 0
    n = len(newspapers)
    read_time = init_time
    req_coworkers = 1
    
    while i < n:
        if newspapers[i] <= read_time:
            read_time -= newspapers[i]
            i += 1
        else:
            read_time = init_time
            req_coworkers += 1
    return req_coworkers <= coworkers

def newspapers_split(newspapers: List[int], coworkers: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    min_ptr = max(newspapers)
    max_ptr = sum(newspapers)
    boundary_index = max_ptr
    
    while min_ptr <= max_ptr:
        mid = (min_ptr + max_ptr)//2
        if feasible(coworkers, mid, newspapers):
            max_ptr = mid - 1
            boundary_index = mid
        else:
            min_ptr = mid + 1
    return boundary_index
from typing import List

def find_min_rotated(arr: List[int]) -> int:
    """ 
    My solution. 
    This makes use of the first element in the array to be compared against the mid instead of the last element.
    This does not work with a non-pivoted array hence the return boundary_index if boundary_index != -1 else 0
    """
    left, right = 0, len(arr)-1
    boundary_index = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= arr[0]:
            left = mid + 1
        else:
            boundary_index = mid
            right = mid - 1
    return boundary_index if boundary_index != -1 else 0
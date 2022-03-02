from typing import List

def peak_of_mountain_array(arr: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left, right = 0, len(arr)-1
    boundary_index = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid+1]:
            boundary_index = mid
            right = mid - 1
        if arr[mid] <= arr[mid+1]:
            left = mid + 1
    return boundary_index


arr = ['0', '1', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '3', '2', '1', '0']
peak_of_mountain_array(arr)
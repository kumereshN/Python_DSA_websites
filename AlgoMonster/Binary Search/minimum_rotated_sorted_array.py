from typing import List

def find_min_rotated(arr: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left, right = 0, len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[-1]:
            left = mid + 1
        else:
            boundary_index = mid
            right = mid - 1
    return boundary_index

arr = [30, 40, 50, 10, 20]
arr_two = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(find_min_rotated(arr_two))
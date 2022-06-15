from typing import List

def remove_duplicates(arr: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    j = 0
    n = len(arr)
    
    for i in range(n):
        if arr[i] != arr[j]:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
    return j + 1
# My Answer
def subarray_sum(arr, target):
    # WRITE YOUR BRILLIANT CODE HERE
    left, right = 0, 0
    total_sum = 0
    n = len(arr)

    while left <= n-1:
        while right <= n-1:
            right += 1
            total_sum = sum(arr[left:right])
            if total_sum == target:
                return [left, right]
        left += 1
        right = left + 1


arr = [1, -20, -3, 30, 5, 7]
target = 7

subarray_sum(arr, target)

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

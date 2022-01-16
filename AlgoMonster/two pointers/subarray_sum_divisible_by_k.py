def subarray_sum_divisible(nums, k):
    left, right = 0, 0
    count = 0
    n = len(nums)

    while left < n:
        while right < n:
            total_sum = sum(nums[left:right+1])
            if total_sum % k == 0:
                count += 1
            right += 1
        right = left + 1
        left = right
    return count


nums = [3, 1, 2, 5, 1]
k = 3
subarray_sum_divisible(nums, k)

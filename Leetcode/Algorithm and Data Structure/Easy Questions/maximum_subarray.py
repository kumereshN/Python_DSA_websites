def maxSubArray(nums):
    n = len(nums)
    curr_sum = max_sum = nums[0]

    for i in range(1, n):
        curr_sum = max(
            nums[i], curr_sum + nums[i]
        )  # Compares against the current number and the sum of current_sum and the current number
        # Compares against the current sum and the previous sum
        max_sum = max(max_sum, curr_sum)
    return max_sum


# Alternative Solution: Dynamic Programming


def maxSubArray(nums):
    n = len(nums)
    max_sum = nums[0]
    for i in range(1, n):
        if nums[i - 1] > 0:  # If the previous index number is positive,
            # If the previous number is positive, add it to the current number. Only the postive numbers are added, no negative numbers
            nums[i] += nums[i - 1]
        # Compare against the current number and the max_sum and use that as the max_sum
        max_sum = max(nums[i], max_sum)
    return max_sum


def maxSubArray(nums):
    maxSub = nums[0]
    curSum = 0

    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSub = max(maxSub, curSum)
    return maxSub

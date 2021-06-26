def maxSubArrayLen(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    seen_sum = {0:0} # Initialise with 0:0 if totalSum == 0
    total_sum = largest_len = 0
    for i in range(len(nums)):
        total_sum += nums[i] # Iterate through the numbers and add to total_sum
        if total_sum == k: # If total_sum matchs k
            largest_len = i + 1 # We've found the largest len
        else: # if total_sum does not equal to k
            required = total_sum - k # What is the required number to add to k
            if required in seen_sum: # If the required number is found in seen_sum
                largest_len = max(largest_len, i - seen_sum[required]) # Get the maximum between largest_len and (index - seen_sum[required])
        if total_sum not in seen_sum: # if total_sum is not found in seen_sum
            seen_sum[total_sum] = i # add {total_sum:index}
    return largest_len

nums = [1,-1,5,-2,3]
k = 3

maxSubArrayLen(nums,k)

"""
A lot of solutions here either put i+1 to history (sum) hashmap or start it with {0: -1}, which makes the code just less maintainable, and to be honest the reason of doing so isn't very obvious.
I just couldn't get my head around that. Following solution solves the same problem without going through that indexing mess.
"""

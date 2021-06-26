def twoSumLessThanK(nums, k):
    nums.sort()
    answer = -1
    left = 0
    right = len(nums) -1
    while left < right:
        sum = nums[left] + nums[right]
        if (sum < k):
            answer = max(answer, sum)
            left += 1
        else:
            right -= 1
    print(answer)
    return answer







nums = [34,23,1,24,75,33,54,8]
k = 60
twoSumLessThanK(nums,k)

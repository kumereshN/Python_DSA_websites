def longestConsecutive(self, nums: List[int]) -> int:
    if not nums:
        return 0

    nums.sort()
    cur = 1
    seq = 1

    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            if nums[i-1]+1 == nums[i]:
                cur += 1
            else:
                seq = max(seq, cur)
                cur = 1
    return max(seq,cur)

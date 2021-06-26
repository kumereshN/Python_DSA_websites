def missingNumber(self, nums: List[int]) -> int:
    num_set = set(nums)
    n = len(nums) + 1

    for num in range(n):
        if num not in num_set:
            return num

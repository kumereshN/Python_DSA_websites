class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float("inf")

        for i in range(len(nums)):
            low, high = i+1, len(nums)-1
            while low < high:
                totalSum = nums[i] + nums[low] + nums[high]
                if abs(target - totalSum) < abs(diff): # Find the smallest difference
                    diff = target - totalSum
                elif totalSum < target:
                    low += 1
                else:
                    high -= 1
            if diff == 0:
                break
        return target - diff

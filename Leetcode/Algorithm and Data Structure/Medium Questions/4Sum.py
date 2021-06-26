from collections import defaultdict
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Store a dp style table of [row][col] for each two sum
        dp = {}
        res = set()
        seen = defaultdict(list)
        # 1
        for r in range(len(nums)):
            for c in range(r):
                have = nums[r] + nums[c]
                need = target - have
                # 2
                if need in seen:
                    # 3
                    for r1,c1 in seen[need]:
                        if len({r1,c1,r,c}) == 4:
                            res.add( tuple(sorted([nums[r1],nums[c1],nums[r],nums[c]])) )
                seen[have].append((r, c))
        return res

"""
Official Solution
"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums,target,k):
            res = []
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return res
            if k == 2:
                return twoSum(nums,target)
            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    for num in kSum(nums[i + 1:], target - nums[i], k-1): # target value becomes reduced for every recursion.
                        res.append([nums[i]] + num) # append the first num in nums in list format + the num list from twoSum. E.g: [-1] + [1,2] = [-1,1,2]
            return res

        def twoSum(nums,target):
            res = []
            low, high = 0, len(nums)-1
            while low < high:
                totalSum = nums[low] + nums[high]
                if totalSum < target or (low > 0 and nums[low] == nums[low-1]):
                    low += 1
                elif totalSum > target or (high < len(nums)-1 and nums[high] == nums[high+1]):
                    high -= 1
                else:
                    res.append([nums[low], nums[high]])
                    low += 1
                    high -=1
            return res

        nums.sort()
        return kSum(nums,target,4)
"""
For python tutor
"""
def fourSum(nums, target):
    def kSum(nums,target,k):
        res = []
        if len(nums) == 0 or nums[0] * k > target or nums[-1] * k < target:
            return res
        if k == 2:
            return twoSum(nums,target)
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                for num in kSum(nums[i+1:],target-nums[i],k-1):
                    res.append([nums[i]] + num)
        return res

    def twoSum(nums,target):
        res = []
        left,right = 0, len(nums)-1
        while left < right:
            totalSum = nums[left] + nums[right]
            if totalSum < target or (left > 0 and nums[left] == nums[left-1]):
                left += 1
            elif totalSum > target or (right < len(nums)-1 and nums[right] == nums[right+1]):
                right -= 1
            else:
                res.append([nums[left],nums[right]])
                left += 1
                right -= 1
        return res

    nums.sort()
    return kSum(nums,target,4)

nums = [1,0,-1,0,-2,2]
target = 0
fourSum(nums,target)

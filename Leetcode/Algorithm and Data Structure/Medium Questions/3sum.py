def threeSum(nums):
    nums.sort()
    ans = set()
    for i,v in enumerate(nums):
        twoSum(nums[i+1:],-v,ans)
    return ans

def twoSum(nums,target,ans):
    d = {}
    for i,v in enumerate(nums):
        if target-v in d:
            ans.add((v,target-v,-target)) #3sum wants the numbers, while 2sum wanted the indices
        d[v] = i

nums = [-1,0,1,2,-1,-4]
threeSum(nums)

# Official Solution: Two pointers
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0: # It has to be a negative number, if not the remaining numbers cannot sum to 0
                break
            if i == 0 or nums[i - 1] != nums[i]: # if it's either the starting number or the previous number is not a duplicate of the current number
                self.twoSumII(nums, i, res) # Go to twoSumII function
        return res

    def twoSumII(self, nums, i, res):
        left, right = i + 1, len(nums) - 1
        while left < right:
            totalSum = nums[i] + nums[left] + nums[right]
            if totalSum < 0:
                left += 1
            elif totalSum > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]: # Check if the low number is not a duplicate of the previous low number
                    left += 1


# Alternative (Most optimal)
def threeSum(nums):
    res = set()
    #1. Split nums into three lists: negative numbers, positive numbers, and zeros
    n, p, z = [], [], []
    for num in nums:
        if num > 0:
            p.append(num)
        elif num < 0:
            n.append(num)
        else:
            z.append(num)

    #2. Create a separate set for negatives and positives for O(1) look-up times
    N, P = set(n), set(p)

    #3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
    #   i.e. (-3, 0, 3) = 0
    if z:
        for num in P:
            if -1*num in N:
                res.add((-1*num, 0, num))

    #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
    if len(z) >= 3:
        res.add((0,0,0))

    #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
    #   exists in the positive number set
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            target = -1*(n[i]+n[j])
            if target in P:
                res.add(tuple(sorted([n[i],n[j],target])))

    #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
    #   exists in the negative number set
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            target = -1*(p[i]+p[j])
            if target in N:
                res.add(tuple(sorted([p[i],p[j],target])))

    return res

nums = [-1,0,1,2,-1,-4]
threeSum(nums)

# My Solution
target = 0
lst = []
nums.sort()

if len(nums) < 3:
    return []
elif all(num == 0 for num in nums):
    return [[0,0,0]]

for i in range(1,len(nums)):
    diff = target - nums[i-1] - nums[i]
    if diff in nums[i:]:
        lst.append([nums[i],nums[i-1],diff])
return lst

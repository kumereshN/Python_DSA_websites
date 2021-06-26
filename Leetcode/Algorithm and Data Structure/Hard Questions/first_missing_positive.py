class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ans = 1
        nums = set(nums)
        while True:
            if ans not in nums:
                return ans
            ans += 1

# Alternative
 def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
     Basic idea:
    1. for any array whose length is l, the first missing positive must be in range [1,...,l+1],
        so we only have to care about those elements in this range and remove the rest.
    2. we can use the array index as the hash to restore the frequency of each number within
         the range [1,...,l+1]
    """
    nums.append(0)
    n = len(nums)
    for i in range(len(nums)): #delete those useless elements
        if nums[i]<0 or nums[i]>=n: # Remove negative numbers and numbers exceeding the length of nums
            nums[i]=0 # Replace with 0
    for i in range(len(nums)): #use the index as the hash to record the frequency of each number
        nums[nums[i]%n]+=n # First loop: nums[1 % 4] += 4 ---> nums[1] += 4
    for i in range(1,len(nums)):
        if nums[i]/n==0: #
            return i
    return n

nums = [1,2,0]
firstMissingPositive(nums)

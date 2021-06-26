# O(n*n) time
def threeSumSmaller(nums, target):
    count = 0
    nums.sort()
    for i in range(len(nums)):
        low, high = i+1, len(nums)-1
        while j < k:
            totalSum = nums[i] + nums[low] + nums[high]
            if totalSum < target:
                # if (i,j,k) works, then (i,j,k), (i,j,k-1),...,
                # (i,j,j+1) all work, totally (k-j) triplets
                count += high-low
                low += 1
            else:
                high -= 1

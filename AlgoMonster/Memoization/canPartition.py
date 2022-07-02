from typing import List

def canPartition(nums: List[int]) -> bool:
        total_sum, n = sum(nums), len(nums)
        # If the total_sum is not an even number, it cannot be split into 2 partitions with the same sum
        if total_sum % 2 != 0:
            return False

        subset_sum = total_sum // 2
        memo = {}               

        def dfs(n, subset_sum):
            state = (n, subset_sum)
            # if the "remaining number" (total_sum being subtracted from a number) is 0, that means there are numbers that can be summed in a partition
            if subset_sum == 0:
                return True
            # If it reaches the end of the list or the "remaining number" becomes 0, return False
            if n == 0 or subset_sum < 0:
                return False

            if state in memo:
                return memo[state]
            # E.g (3,11):(True), (2,6):(False)
            memo[state] = (dfs(n - 1, subset_sum - nums[n]) or dfs(n - 1, subset_sum))

            return memo[state]

        return dfs(n - 1, subset_sum)

# nums = [1,5,11,5]
nums = [1,2,3,5]
print(canPartition(nums))

""" Source: https://leetcode.com/problems/partition-equal-subset-sum/ """
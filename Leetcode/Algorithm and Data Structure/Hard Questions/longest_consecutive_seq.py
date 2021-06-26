class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]: # If the cur num and the prev num are not duplicates
                if nums[i] == nums[i-1]+1: # If numbers are consecutive
                    current_streak += 1 # Increment current_streak
                else: # If the numbers are not consecutive
                    longest_streak = max(longest_streak, current_streak) # current_streak becomes the longest_streak or whichever is the higest number
                    current_streak = 1 # current_streak resets to 1

        return max(longest_streak, current_streak) # get the max between longest_streak and current_streak

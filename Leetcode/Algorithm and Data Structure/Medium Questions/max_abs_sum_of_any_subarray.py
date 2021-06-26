class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_so_far, pos_ending_here, neg_ending_here = 0, 0, 0
        for num in nums:
            pos_ending_here = max(0, pos_ending_here + num)
            neg_ending_here = min(0, neg_ending_here + num)
            max_so_far = max(max_so_far, pos_ending_here, -neg_ending_here)
        return max_so_far

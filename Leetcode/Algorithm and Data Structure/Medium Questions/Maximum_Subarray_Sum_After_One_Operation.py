class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        prev_square = prev_no_square = res = 0
        for num in nums:
            no_square = max(num, num+prev_no_square) # Get the maximum between current num and num + prev_no_square, which is adding the subarray
            square = max(num*num, num*num+prev_no_square, num+prev_square) # 3 Possibilties: Get the max between with square of num, square of num + prev_no_square and num + prev_square
            res = max(res, square) # Get the maximum between res and square
            prev_square, prev_no_square = square, no_square

        return res


# Approach 1 - Extending Kadane's algo to this case.

class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        ans = f0 = f1 = 0
        for x in nums:
            f1 = max(max(0, f0) + x*x, f1 + x)
            f0 = max(0, f0) + x
            ans = max(ans, f1)
        return ans

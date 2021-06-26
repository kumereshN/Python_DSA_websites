# Official Solution
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Create hashmap
        For each number in nums1.
            hashmap[nums1[i]] = i + 1
        For each number in nums2.

        """
        A = nums1
        B = nums2

        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)] # [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        for i in range(len(A) - 1, -1, -1): # range(5-1,-1,-1), it's in reverse format
            for j in range(len(B) - 1, -1, -1): # range(5-1,-1,-1), starting from 4th index not 5th index, reverse it.
                if A[i] == B[j]: # If the numbers match
                    memo[i][j] = memo[i+1][j+1]+1 # Get the previous list (i+1), in that list, get the number in j+1 index and add 1. Store in memo[i][j]
        return max(max(row) for row in memo)

nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
findLength(nums1,nums2)

class Solution:
	def findLength(self, A: List[int], B: List[int]) -> int:

		m = len(nums1)
        n = len(nums2)

        if m == 0 or n == 0:
            return 0

        if m == 1 and n == 1:
            if nums1[m] == nums2[n]:
                return 1
            else:
                return 0

        dp = [[0 for y in range(n+1)] for x in range(m+1)]
        final = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 0

                final = max(final, dp[i][j])

        return final

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        if k >= len(prices)//2:
            return sum([i - j for i,j in zip(prices[1:],prices[:-1]) if i-j>0])


        dp = [[0]*len(prices) for _ in range(k+1)]

        for act in range(1,k+1):
            max_val = float('-inf')
            for day in range(1, len(prices)):
                max_val = max(max_val, dp[act-1][day-1] - prices[day-1])
                dp[act][day] = max(max_val+prices[day], dp[act][day-1])

        return dp[-1][-1]


"""
this video explains the algorithm.
https://www.youtube.com/watch?v=oDhu5uGq_ic
"""

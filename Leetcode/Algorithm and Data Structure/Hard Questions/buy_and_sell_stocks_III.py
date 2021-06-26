class Solution(object):
    def maxProfit(prices):
        # dynamic programming
        first_buy, first_profit, second_buy_first_porfit, max_profit = float('inf'), 0, float('inf'), 0
        for price in prices:
            first_buy = min(first_buy, price)
            first_profit = max(first_profit, price-first_buy)
            second_buy_first_porfit = min(second_buy_first_porfit, price-first_profit) # Buy on the same day after taking first profit. This will reduce the first profit because we buy again on the same day after selling on the same day.
            max_profit = max(max_profit, price-second_buy_first_porfit)
        return max_profit

prices = [1,2,4,2,5,7,2,4,9]
maxProfit(prices)

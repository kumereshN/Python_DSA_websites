class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_day_to_buy = 0
        maxprofit = 0
        for i in range(1, len(prices)):
            """
            Suppose we sell our stock at day i:
            in order to maximize our profit
            we need to buy the stock on the day when the stock price is
            the lowest from day 0 to day i-1.
            """
            if(prices[lowest_day_to_buy] > prices[i - 1]): # If the price of the lowest_day is greater than the next day's price
                lowest_day_to_buy = i - 1 # Decrement the lowest_day_to_buy
            # get the overall max profit by comparing all the max profits if we sold
            # our stock on day n (1 <=n < len(prices))
            maxprofit = max(maxprofit, prices[i] - prices[lowest_day_to_buy])
        return maxprofit


# Alternative
def maxProfit(self, prices: List[int]) -> int:
	if not prices:
		return 0

	maxProfit = 0
	minPurchase = prices[0] # First price
	for i in range(1, len(prices)):
		maxProfit = max(maxProfit, prices[i] - minPurchase) # Compare the current max profit against (next day's price - today's price) and then get the max price and set it as the max price
		minPurchase = min(minPurchase, prices[i]) # Compare the current minPurchase against next day's price and get the minPurchase and set as the minPurchase
	return maxProfit


    # Notes
    # For maxProfit: you buy today and sell tomorrow, what is the profit?
    # For minPurchase: Compare against the current minPurchase with the price next day, which is the smaller number?
    # For minPurcase: We want to retain the smallest number and sell it later as the highest number on that day

# Alternative
def maxProfit(prices):
	minPrice = math.inf
    maxProfit = 0
    for i in prices:
        minPrice = min(i, minPrice)
        maxProfit = max(i - minPrice, maxProfit)
    return maxProfit


# Alternative
def maxProfit(prices):
    if len(prices) == 0:
        return 0
    else:
        low = float("inf")
        profitmax = 0
        for price in prices:
            if price > low:
                if price - low > profitmax:
                    profitmax = price - low
            elif price < low:
                low = price
    
        return profitmax

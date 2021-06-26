# Official Solution
def maxProfit(prices) :
    sold, held, reset = float('-inf'), float('-inf'), 0

    for price in prices:
        pre_sold = sold
        sold = held + price # Sold the stock before reaching this state. Agent has no stock. If I sell, I'll get this profit.
        held = max(held, reset - price) # Bought a stock held before
        reset = max(reset, pre_sold) # Starting point. Agent holds no stock and has not sold the stock previously.
    return max(reset, sold)

prices = [1,2,3,0,2]
maxProfit(prices)

"""
sold[i]: the previous state of sold can only be held. Therefore, the maximal profits of this state is the maximal profits of the previous state plus the revenue by selling the stock at the current price.

held
held[i]: the previous state of held could also be held, i.e. one does no transaction. Or its previous state could be reset, from which state, one can acquire a stock at the current price point.

reset
reset[i]: the previous state of reset could either be reset or sold. Both transitions do not involve any transaction with the stock.


Finally, the maximal profits that we can gain from this game would be max(sold,reset).

max(sold[n],reset[n]), i.e. at the last price point, either we sell the stock or we simply do no transaction, to have the maximal profits.
It makes no sense to acquire the stock at the last price point, which only leads to the reduction of profits.
"""


# Alternative
def maxProfit(prices):
    free = 0
    have = cool = float('-inf')
    for price in prices:
        free, have, cool = max(free, cool), max(have, free - price), have + price # Start from cool to free order.
    return max(free, cool)


prices = [1,2,3,0,2]
maxProfit(prices)

"""
free is the maximum profit I can have while being free to buy.
have is the maximum profit I can have while having stock.
cool is the maximum profit I can have while cooling down.
"""

"""
@StefanPochmann
This is very smart.

@stone30
Let me just expand what StefanPochmann explained a little bit:
free is the maximum profit I can have while being free to buy.
I am free to buy in the current iteration either because I was free to buy in the previous iteration and did nothing in the current iteration, or I was cooling down in the previous iteration and did nothing in the current iteration.

have is the maximum profit I can have while having stock,
i.e., I've bought a stock and haven't sold it yet. This happens when I was already holding stock but did not sell in this iteration, or I was free to buy stock last iteration and bought the stock in the current iteration.

cool is the maximum profit I can have while cooling down.
This only happens if I was holding a stock in the previous iteration and sold it in the current iteration.
"""

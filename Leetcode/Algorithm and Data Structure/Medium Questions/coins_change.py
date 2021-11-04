def coinChange(coins, amount):
    need = [0] + [amount + 1] * amount
    for a in range(min(coins), amount + 1):
        need[a] = min([need[a - c] for c in coins if c <= a]) + 1
    return need[-1] if need[-1] <= amount else -1


""" Dynamic programming with need[a] telling the number of coins needed for amount a.
 "Not (yet) possible" is represented by amount + 1, since the worst actually possible solution is amount coins (each having value 1). """

""" I prefer min( ... ) over min([ ... ]), but generators tend to be slower than list comprehensions, and here I wanted fast.

   Starting a at min(coins) is a little optimization and more importantly prevents min from getting nothing and erroring on me (I know, I know... it would still fail if there were an input with no coins... if there were, I'd probably prefix the loop with if coins:).
   """


# Breadth-first solution
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        queue = [[0, 0]]
        visited = {0}
        step = 0
        for node, step in queue:
            for coin in coins:
                if node + coin in visited:
                    continue
                if node + coin == amount:
                    return step + 1
                elif node + coin < amount:
                    queue.append([node + coin, step + 1])
                    visited.add(node + coin)
        return -1

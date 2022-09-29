def dfs(coins, start, remaining, path):
    n = len(coins)
    
    if remaining == 0:
        res.append(len(path[:]))
        return
    
    for i in range(start, n):
        coin = coins[i]
        if remaining - coin < 0:
            continue
        dfs(coins, i, remaining - coin, path + [coin])
    
coins = [1,2,5]
amount = 11
res = []

dfs(coins, 0, amount, [])
print(min(res))
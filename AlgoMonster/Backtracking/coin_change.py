def dfs(coins, start, remaining, path, res):
    n = len(coins)
    
    if remaining == 0:
        res.append(path[:])
        return
    
    for i in range(start, n):
        coin = coins[i]
        if remaining - coin < 0:
            continue
        dfs(coins, i, remaining - coin, path + [coin], res)
    
coins = [1,2,5]
amount = 11
memo = dict()
res = []

dfs(coins, 0, amount, [], res)
print(res)
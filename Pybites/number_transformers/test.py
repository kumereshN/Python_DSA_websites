def num_ops(n):
    dp = [float('inf')] * (n+1)
    dp[1] = 0
    for curr in range(2, n+1):
        if curr % 3 == 0:
            dp[curr] = min(dp[curr // 3], dp[curr // 2], dp[curr - 1]) + 1
        elif curr % 2 == 0:
            dp[curr] = min(dp[curr // 2], dp[curr - 1]) + 1
        else:
            dp[curr] = dp[curr - 1] + 1
    return dp[n]


print(num_ops(10))
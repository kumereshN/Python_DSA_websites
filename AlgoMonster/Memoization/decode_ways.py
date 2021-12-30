def decode_ways(digits: str) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    prefixes = [str(x) for x in range(1, 27)]
    memo = {}

    def dfs(i):
        if i == len(digits):
            return 1
        if i in memo:
            return memo[i]

        ways = 0
        remaining = digits[i:]

        for prefix in prefixes:
            if remaining.startswith(prefix):
                ways += dfs(i + len(prefix))
        memo[i] = ways
        return ways

    return dfs(0)

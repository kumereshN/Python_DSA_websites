def decode_ways(digits: str) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    prefixes = [str(i) for i in range(1, 27)]

    def dfs(i, memo):
        # If index reaches the end of the digits, return 1
        if i == len(digits):
            return 1
        if i in memo:
            return memo[i]

        ways = 0
        remaining = digits[i:]
        for prefix in prefixes:
            if remaining.startswith(prefix):
                # len(prefix) is always 1, so increment i by 1
                ways += dfs(i + len(prefix), memo)
        memo[i] = ways
        return ways
    return dfs(0, {})

def decode_ways(digits: str) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    prefixes = [str(i) for i in range(1,27)]
    memo = {}
    
    def dfs(i):
        if i in memo:
            return memo[i]
        if i == len(digits):
            return 1
        
        ways = 0
        
        for prefix in prefixes:
            if digits[i:].startswith(prefix):
                ways += dfs(i + len(prefix))
                
        memo[i] = ways
        return ways
    return dfs(0)
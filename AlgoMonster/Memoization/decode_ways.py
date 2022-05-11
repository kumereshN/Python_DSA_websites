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
        num = digits[i:]
        
        for prefix in prefixes:
            if num.startswith(prefix):
                ways += dfs(i + len(prefix))
                
        memo[i] = ways
        return memo[i]
    return dfs(0)

digits = "123"
decode_ways(digits)

"""
How the backtracking is done
First part: '1', '2', '3'
Second part: '12', '3'
Third part: '1', '23'

Once i reaches the end of the digits, increment the ways by 1
"""
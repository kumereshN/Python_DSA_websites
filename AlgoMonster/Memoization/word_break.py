def word_break(s, words):

    memo = {}

    def dfs(i):
        # Base case: if we reach the end of the string
        if i == len(s):
            return True
        # Base case: If we've seen the index before, return the boolen value
        if i in memo:
            return memo[i]
        ok = False
        for word in words:
            # if the string[i:] starts with the word
            # checking if this is a valid path
            if s[i:].startswith(word):
                # current index + len(word)
                # Does the recursion to check the above 2 base cases
                if dfs(i + len(word)):
                    ok = True
                    break
        memo[i] = ok
        return ok

    return dfs(0)


s = 'algomonster'
words = ['algo', 'monster']

word_break(s, words)

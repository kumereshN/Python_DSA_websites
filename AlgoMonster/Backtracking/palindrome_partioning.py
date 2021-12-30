def partition(s):
    # WRITE YOUR BRILLIANT CODE HERE
    ans = []

    n = len(s)

    def is_palindrome(s):
        return s == s[::-1]

    def dfs(start, cur_path):
        """
        cur_path is the state
        """
        # Base case: we've reached the end of the string
        # Appending all the palindrome partioning to the ans list
        # start is the index of the string which is carried over to the next recursion
        if start == n:
            ans.append(cur_path)
            return

        for i in range(start+1, n+1):
            # Obtaining the prefix
            prefix = s[start:i]
            # Only continue if the substring is a palindrome (This is call pruning the state space branches)
            if is_palindrome(prefix):
                # If it's a palindrome, added it to the cur_path list
                dfs(i, cur_path + [prefix])

    dfs(0, [])
    return ans


s = 'aab'
partition(s)

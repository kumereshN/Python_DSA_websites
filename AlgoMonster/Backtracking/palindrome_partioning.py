from typing import List

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
            ans.append(cur_path[:])
            return

        for i in range(start+1, n+1):
            # Obtaining the prefix
            # start does not increment until it reaches is_palindrome
            prefix = s[start:i]
            # Only continue if the substring is a palindrome (This is call pruning the state space branches)
            if is_palindrome(prefix):
                # If it's a palindrome, added it to the cur_path list
                dfs(i, cur_path + [prefix])

    dfs(0, [])
    return ans


def partition(s: str) -> List[List[str]]:
    # WRITE YOUR BRILLIANT CODE HERE
    """
    Alternative
    """
    res = []
    n = len(s)
    
    def is_palindrome(word):
        return word == word[::-1]
    
    def dfs(start, path):
        if start == n:
            res.append(path)
            return
            
        for end in range(start+1, n+1):
            prefix = s[start:end]
            if is_palindrome(prefix):
                path.append(prefix)
                dfs(end, path[:])
                path.pop()
    
    dfs(0, [])
    return res

s = 'aab'
print(partition(s))

# def word_break(s, words):

#     memo = {}

#     def dfs(i):
#         # Base case: if we reach the end of the string
#         if i == len(s):
#             return True
#         # Base case: If we've seen the index before, return the boolen value
#         if i in memo:
#             return memo[i]
#         ok = False
#         # checks each word, does the string start with the word
#         for word in words:
#             # checking if this is a valid path
#             # Example: starts with index on 'a' in s = 'algo' checks whether it startswith the word, does the dfs, moves the index to 'm' for the next word to become s = 'monster'
#             if s[i:].startswith(word):
#                 # checks for the next word in the words list
#                 # Does the recursion to check the above 2 base cases
#                 if dfs(i + len(word)):
#                     # If all the words in the word list matches the string, then set the boolean value to be True
#                     ok = True
#                     # break out of the for loop
#                     break
#         # Caches the index of the first letter in each word in the word list with boolean values on whether they start in the string s.
#         memo[i] = ok
#         return ok

#     return dfs(0)


# s = 'algomonster'
# words = ['algo', 'monster']

# word_break(s, words)

# Alternative

from typing import List

def word_break(s: str, words: List[str]) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    memo = {}
    
    def dfs(i):
        if i in memo:
            return memo[i]
        if i == len(s):
            return True
        
        for word in words:
            prefix = s[i:]
            if prefix.startswith(word):
                if dfs(i + len(word)):
                    # If all the words in the word list match with the String, end the statement with True
                    return True
        # working backwards, prefix ends with 'b', then 'ab', then 'aab' which all does not match with the words list
        # hence, returning False 
        memo[i] = False
        return memo[i]
    return dfs(0)


s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'
words = ['a', 'aa','aaa','aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']

print(word_break(s, words))
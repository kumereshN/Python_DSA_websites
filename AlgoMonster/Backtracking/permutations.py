"""
User Solution
"""
# def permutations(l):
#     # WRITE YOUR BRILLIANT CODE HERE
#     if not l:
#         return []
#     res = []
#     permutation = []

#     def dfs(l, permutation):
#         # Base case
#         if len(permutation) == len(l):
#             # We're making a copy of the list to be appended to res as the list will be changed in subsequent recursions
#             res.append(list(permutation))
#             # Exit out of the recursion
#             return

#         for letter in l:
#             if letter not in permutation:
#                 permutation.append(letter)
#                 dfs(l, permutation)
#                 # Backtracking
#                 permutation.pop()

#     dfs(l, permutation)
#     return res


# if __name__ == "__main__":
#     res = permutations(list(input()))
#     print(' '.join(sorted(''.join(x) for x in res)))

"""
Algo monster solution
"""

from typing import List

def permutations(l):
    """
    There are 2 things to note here:
    the path is a list that keeps getting updated inside the dfs function
    the res is a list that outputs all the permuatations
    """
    def dfs(path):
        if len(path) == len(l):
            res.append(''.join(path))
            return

        for letter in l:
            # skip used letters
            if letter in path:
                continue
            # add letter to permutation, mark letter as used
            path.append(letter)
            dfs(path)
            # remove letter from permutation, mark letter as unused
            path.pop()

    res = []
    dfs([])
    return res

letters = 'abc'
print(permutations(letters))
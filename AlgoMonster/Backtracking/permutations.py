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

def permutations(letters):
    def dfs(path, used, res):
        if len(path) == len(letters):
            res.append(''.join(path))
            return

        for i, letter in enumerate(letters):
            # skip used letters
            if used[i]:
                continue
            # add letter to permutation, mark letter as used
            path.append(letter)
            used[i] = True
            dfs(path, used, res)
            # remove letter from permutation, mark letter as unused
            path.pop()
            used[i] = False

    res = []
    dfs([], [False] * len(letters), res)
    return res

letters = 'abc'
print(permutations(letters))
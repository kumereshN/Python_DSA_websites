def permutations(l):
    # WRITE YOUR BRILLIANT CODE HERE
    if not l:
        return []
    res = []
    permutation = []

    def dfs(l, permutation):
        # Base case
        if len(permutation) == len(l):
            # We're making a copy of the list to be appended to res as the list will be changed in subsequent recursions
            res.append(list(permutation))
            # Exit out of the recursion
            return

        for letter in l:
            if letter not in permutation:
                permutation.append(letter)
                dfs(l, permutation)
                # Backtracking
                permutation.pop()

    dfs(l, permutation)
    return res


if __name__ == "__main__":
    res = permutations(list(input()))
    print(' '.join(sorted(''.join(x) for x in res)))

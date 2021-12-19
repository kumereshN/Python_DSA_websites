def permutations(l):
    # WRITE YOUR BRILLIANT CODE HERE
    if not l:
        return []
    res = []
    permutation = []

    def dfs(l, permutation, res):
        # Base case
        if len(permutation) == len(l):
            res.append(list(permutation))
            # Exit out of the recursion
            return

        for letter in l:
            if letter not in permutation:
                permutation.append(letter)
                dfs(l, permutation, res)
                # Backtracking
                permutation.pop()

    dfs(l, permutation, res)
    return res


if __name__ == "__main__":
    res = permutations(list(input()))
    print(' '.join(sorted(''.join(x) for x in res)))

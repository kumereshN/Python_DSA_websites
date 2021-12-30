def subsets(nums):
    # WRITE YOUR BRILLIANT CODE HERE
    res = []

    # The path carries the state to the next recursion
    def dfs(i, path):
        # Base case: if the index is the len(nums), append the path to result
        if i == len(nums):
            res.append(path)
            return
        # DFS as normal
        dfs(i+1, path + [nums[i]])
        # this backtracks to the previous node, and checks for other combinations from the nums
        # Example [1,2] and [1,3]
        dfs(i+1, path)
    dfs(0, [])
    return res


nums = [1, 2, 3]
subsets(nums)

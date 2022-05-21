def subsets(nums):
    # WRITE YOUR BRILLIANT CODE HERE
    res = [[]]

    # The path carries the state to the next recursion
    def dfs(i, path):
        # Base case: if the index is the len(nums)
        # it goes back to the previous stack, e.g: i = 3 then falls back to 2
        if i == len(nums):
            return
        # DFS as normal
        num = nums[i]
        res.append(path + [num])
        dfs(i+1, path + [num])
        # this backtracks to the previous node, and checks for other combinations from the nums
        # Example [1,2] and [1,3]
        dfs(i+1, path)
    dfs(0, [])
    return res


nums = [1, 2, 3]
print(subsets(nums))

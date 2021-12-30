from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    # WRITE YOUR BRILLIANT CODE HERE
    res = []
    n = len(candidates)

    def dfs(start, nums, remaining, path):
        if remaining == 0:
            res.append(path[:])
            return
        # start_index is to keep track of the index moving, if not it'll reset to 0 everytime it does dfs
        for i in range(start, n):
            num = nums[i]
            # If remaining - num is less than 0, we prune the branch
            # if the remaining - num is less than 0, we move to the next number in the list
            if remaining - num < 0:
                continue
            # Carry i to the next recursion
            dfs(i, nums, remaining - num, path + [num])
        return res
    return dfs(0, candidates, target, [])

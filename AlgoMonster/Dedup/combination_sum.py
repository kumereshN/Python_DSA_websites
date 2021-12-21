from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    def dfs(start_index, nums, remaining, path):
        if remaining == 0:
            res.append(path[:])
            return
        # start_index is to keep track of the index moving, if not it'll reset to 0 everytime it does dfs
        for i in range(start_index, len(nums)):
            num = nums[i]
            # If remaining - num is less than 0, we prune the branch
            if remaining - num < 0:
                continue
            dfs(nums, i, remaining - num, path + [num])
    res = []
    dfs(0, candidates, target, [])
    return res

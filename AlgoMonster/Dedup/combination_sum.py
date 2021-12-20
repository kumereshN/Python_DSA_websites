from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    def dfs(nums, start_index, remaining, path):
        if remaining == 0:
            res.append(path[:])
            return
        for i in range(start_index, len(nums)):
            num = nums[i]
            # If remaining - num is less than 0, we prune the branch
            if remaining - num < 0:
                continue
            dfs(nums, i, remaining - num, path + [num])
    res = []
    dfs(candidates, 0, target, [])
    return res

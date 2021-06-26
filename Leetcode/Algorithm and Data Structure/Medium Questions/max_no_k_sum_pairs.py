from collections import defaultdict


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        pair = defaultdict(int) # integer 0 is the default value of all the keys
        res = 0

        for n in nums:
            if pair[n]: # if we encountered k - n already
                res += 1
                pair[n] -= 1
            else: # if we did'n find a pair yet
                pair[k - n] += 1

        return res

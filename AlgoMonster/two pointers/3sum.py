from typing import List


def triplets_with_sum_0(nums: List[int]) -> List[List[int]]:
    # WRITE YOUR BRILLIANT CODE HERE
    nums.sort()

    n = len(nums)
    res = []
    for i in range(n - 2):
        # handle duplicates with these 3 lines
        # note: only need to check for i and i-1.
        # (left, right) won't throw duplicates since
        # they are moved on each iteration
        if i == 0 or nums[i] != nums[i - 1]:
            left = i + 1
            right = n - 1
            while left < right:
                x, y, z = nums[i], nums[left], nums[right]
                total_sum = x + y + z
                if total_sum == 0:
                    res.append([x, y, z])
                    left += 1
                    right -= 1
                elif total_sum < 0:
                    left += 1
                else:
                    right -= 1

    return res


from typing import List

def triplets_with_sum_0(nums: List[int]) -> List[List[int]]:
    """
    Doing it with recursion, backtracking
    """
    # WRITE YOUR BRILLIANT CODE HERE
    n = len(nums)
    required_numbers = 6
    target_sum = 1
    nums.sort()
    res = []
    def dfs(start, path):
        # Base Case
        if len(path) == required_numbers and sum(path) == target_sum and path not in res:
            res.append(path)
            return
        elif len(path) == required_numbers:
            return

        for i in range(start, n):
            dfs(i+1, path + [nums[i]])
    
    dfs(0, [])
    return res
    
# nums = [1, -1, 2, -2, 3, -3, 4, -4]
nums =  [-4, 0, 4, 0, 3, 0, -1, -2, 0, 2, -2]
print(triplets_with_sum_0(nums))
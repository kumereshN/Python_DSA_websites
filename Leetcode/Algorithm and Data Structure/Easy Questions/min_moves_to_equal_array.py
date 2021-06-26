def minMoves(nums):
    res = 0
    nums.sort()
    for i in range(1, len(nums)):
        res += nums[i] - nums[0]
    return res


# Alternative
def minMoves(nums):
    minNo = min(nums)
    moves = 0

    for no in nums:
        moves += no - minNo

    return moves

def twoSum(nums, target):
    prevMap = {}  # val : index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i


nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))

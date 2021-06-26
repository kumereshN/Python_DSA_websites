'''
we can define a "group" relationship on the integers
(refer: https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/congruence-modulo)
if the results of two integers i1 and i2 modulo k are the same, then we can say they are in the same group
e.g. 7 % 13 = 7 and 46 % 13 = 7, so we can think of 7 and 46 are in the same group
we can name the group using the result of modulo
if we know two integers i1 and i2 are in the same group d, then we have:
i1 = 13 * a + d and i2 = 13 * b + d where a and b are both integers
if then we calculate their difference, we can get:
i1 - i2 = 13 * a - 13 * b + d - d = 13 * (a - b)
since a and b are both integers, (a - b) must be integers as well
Conclusion: if two integers are in the same group, their difference must be divisible by the divisor k
Now back to prefix sum, if we know that the difference of two prefix sum is divisible by k, then we
can learn that sum of the subarray corresponds to this difference must be divisible by k (aka, it is
multiple of k
''''

def checkSubarraySum(nums, k):
    presum = dict()
    presum[0] = -1

    totalSum = 0

    for idx, num in enumerate(nums):
        totalSum += num # Add the num to totalSum
        if k != 0:
            totalSum %= k # Finding the modulo

        if totalSum in presum: # If the modulo in presum, then we've found a match
            if idx - presum[totalSum] >= 2: # The number of elements is more than or equal to 2
                return True
        else:
            presum[totalSum] = idx # Initialise modulo:index
    return False

nums = [23,2,4,6,7]
k = 6
checkSubarraySum(nums,k)

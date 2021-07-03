"""
Explanation
Compare all neignbour elements (a,b) in A,
the case of a > b can happen at most once.

Note that the first element and the last element are also connected.

If all a <= b, A is already sorted.
If all a <= b but only one a > b,
we can rotate and make b the first element.
Other case, return false.


Complexity
Time O(n)
Space O(1)
"""


def check(self, A):
    return sum(nums[i] < nums[i - 1] for i in range(len(nums))) <= 1


nums = [3, 4, 5, 1, 2]
check(nums)

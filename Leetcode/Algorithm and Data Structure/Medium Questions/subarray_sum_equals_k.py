# More pythonic version
from collections import defaultdict


def subarraySum(nums, k):
    count = totalSum = 0
    running_sum = defaultdict(int)
    running_sum[0] = 1  # initialise 0

    for n in nums:
        totalSum += n
        count += running_sum[
            totalSum - k
        ]  # We found a subarray of sums = k, so count += running_sum[sum-k]
        running_sum[totalSum] += 1  # Just like twoSums. number:count

    return count


nums = [1, 1, 1]
k = 2
subarraySum(nums, k)


"""
Just wanted to share a clear explanation that helped me.

First of all, the basic idea behind this code is that, whenever the sums has increased by a value of k, we've found a subarray of sums=k.
I'll also explain why we need to initialise a 0 in the hashmap.
Example: Let's say our elements are [1,2,1,3] and k = 3.
and our corresponding running sums = [1,3,4,7]
Now, if you notice the running sums array, from 1->4, there is increase of k and from 4->7, there is an increase of k. So, we've found 2 subarrays of sums=k.

But, if you look at the original array, there are 3 subarrays of sums==k. Now, you'll understand why 0 comes in the picture.

In the above example, 4-1=k and 7-4=k. Hence, we concluded that there are 2 subarrays.
However, if sums==k, it should've been 3-0=k. But 0 is not present in the array. To account for this case, we include the 0.
Now the modified sums array will look like [0,1,3,4,7]. Now, try to see for the increase of k.

0->3
1->4
4->7
Hence, 3 sub arrays of sums=k
This clarified some confusions I had while doing this problem.
"""


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        sums = 0
        d = dict()
        d[0] = 1

        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums - k, 0)
            d[sums] = d.get(sums, 0) + 1

        return count

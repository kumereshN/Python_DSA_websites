# Offical solution
# Return how many numbers are missing until nums[idx]
        missing = lambda idx: nums[idx] - nums[0] - idx

        n = len(nums)
        # If kth missing number is larger than
        # the last element of the array
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1)

        idx = 1
        # find idx such that
        # missing(idx - 1) < k <= missing(idx)
        while missing(idx) < k:
            idx += 1

        # kth missing number is greater than nums[idx - 1]
        # and less than nums[idx]
        return nums[idx - 1] + k - missing(idx - 1)

# Alternative solution
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:


        #Approach:
        # Step 1: find maximum possible kth number provided we had only one digit in array.
        # it will be (nums[0] + k)


        # Step2: nums[0] + k would have been the answer if there were no other digits, but if we have than we need to find number of digits which are less than nums[0] + k.




        # what is the kth missing number for single digit x, it is x + k
        ans = nums[0] + k

        # if lenght is one then x + k will be the answer
        if len(nums) == 1:
            return ans

        # if length is greater than one, we try to find how many numbers are less than
        # the maximum possible kth missing number (x+k)
        # whenever we encounter that there exist a number that is less than (x+k) we increase the (x+k) by 1
        # as soon as our ans (x+k) is greater than any number in the list, we return ans.
        for num in nums[1:]:

            if num > ans:
                return ans
            elif num <= ans:
                ans +=1

        return ans

nums = [4,7,9,10]
k = 1

missingElement(arr,k)

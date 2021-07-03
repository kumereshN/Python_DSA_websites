class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        arr = [0, 1]
        for i in range(2, n + 1):
            if i % 2 == 0:
                arr.append(arr[i // 2])
            else:
                arr.append(arr[i // 2] + arr[i // 2 + 1])
        return max(arr)


"""
The Basic Idea is that given our constraints and the Question itself, we can simply just generate the array by simulating what is needed. So, we start with our base array of [0, 1] and for any N > 1 we generate the array as following:

If our index is even: we divide the index by 2 and append that result to our base array.
If our index is odd: we divide the index by 2 ( and considering only the integer of it, so 7//2 = 3 and not 3.5 ) and use that index and the next of that index.
We hence generate the entire array from 0 to N, so N+1 elements, and our job now is to only find the maximum of this array.

Note: This takes a O(N) time and O(N) space in generating the array.
"""

def findKthPositive(arr, k):
    for idx, num in enumerate(arr):
        if num > idx + k:  # For missing numbers in an array, for each number in the array, check if the num > idx + k
            return idx + k
    # If there are no missing numbers in the array, then get the length of the array + k
    return len(arr) + k


arr = [2, 3, 4, 7, 11]
k = 5
findKthPositive(arr, k)

"""
Explanation:
But wait... Do we really need a counter? If there is no missing number, the a[i] should just be i+1.
If there is a single missing number before a[i], a[i] should be just i+2. So on so forth.
In general, if there are m missing numbers up to a[i], a[i] = i + m + 1.
So, when we see a[i], we know there are a[i]-i-1 missing numbers up to it.
If a[i]-i-1 >= k or a[i] > i+k, the k-th missing value must be between a[i-1] and a[i].

On the other hand, if there have already been i numbers in a, the k-th missing value must be at least k+i.
We show that k+i is actually the value we are looking for. First, a[i] > i+k, so i+k cannot be a[i].
Neither can it be any a[j], j > i, becausue a is increasing and a[j] > a[i] > i+k.
Can i+k appear before a[i]? If that is the case, say i+k = a[j] for some j < i, then we will have a[j] = i+k > j+k.
That means we would have found an earlier location j that triggers the a[j] > j+k criterion, and we would have stopped over there.

The above analysis gives us this clean 4 lines of code.
"""

# Alternative


def findKthPositive(arr, k):
    ## RC ##
    ## APPROACH : BINARY SEARCH ##
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (hi + lo) // 2
        missing = arr[mid] - (
            mid + 1
        )  # ideally, arr[i] should hold i + 1 value i.e arr[0] = 1, arr[1] = 2..etc
        if missing >= k:  # If the missing number is more than or equal to k
            hi = mid - 1  # Then the missing kth number must be on the left side
        else:
            lo = mid + 1
    return (
        hi + k + 1
    )  # Goes to the 3rd index of [2,3,4,7,11] which is 7 + kth index which is 5 + 1 = 9 the missing number


"""
Missing no: 4-3= 1, middle no - (mid index + 1) = 4 - 3 = 1

arrays without missing integers = [1,2,3,4,5]
input array = [2,3,4,7,11]
2-1 = 1 missing integer
3-2 = 1 missing integer
4-3 = 1 missing integer
"""

"""
Goes to the closest number (high) in the array towards kth index. Then, high + k + 1 to find the missing number
"""

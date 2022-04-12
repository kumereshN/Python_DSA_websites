from typing import List


def numberOfSubarrays(nums, k):
    right, left = 0, 0
    ans = 0
    cur_sub_cnt = odd_cnt = 0
    for right in range(len(nums)):
        # if we've found a odd number, increment the odd counter and reset the cur_sub_cnt to 0
        if nums[right] % 2 == 1:
            odd_cnt += 1
            cur_sub_cnt = 0
        # The right side of the window is incremented until we've found odd_cnt == k
        # This is when we've found a window
        while odd_cnt == k:
            # Minimize the window until we've found a odd number 
            if nums[left] % 2 == 1:
                odd_cnt -= 1
            cur_sub_cnt += 1
            # Move to the next number after the finding the odd number
            left += 1
        # The ans continues to be incremented with the cur_sub_cnt until we've found another odd number
        # This means a new window is found
        ans += cur_sub_cnt
    return ans


def count_nice_subarrays(k, arr):

    left = 0
    result = 0
    final_array = []

    while left < len(arr) - k + 1:
        right = left
        sub_array = []
        num_odd = k
        while num_odd and right < len(arr):
            sub_array.append(arr[right])
            if arr[right] % 2 != 0:
                num_odd -= 1
            right += 1
            if num_odd == 0 and sub_array:
                result += 1
        final_array.append(sub_array)
        left += 1
    print(final_array)
    return result

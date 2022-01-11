from typing import List


def numberOfSubarrays(nums, k):
    right, left = 0, 0
    ans = 0
    odd_cnt = 0
    ans = 0
    cur_sub_cnt = 0
    for right in range(len(nums)):

        if nums[right] % 2 == 1:
            odd_cnt += 1
            cur_sub_cnt = 0

        while odd_cnt == k:
            if nums[left] % 2 == 1:
                odd_cnt -= 1
            cur_sub_cnt += 1
            left += 1

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

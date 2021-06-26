def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    for i in range(n):
        nums1[i + m] = nums2[i]

    nums1.sort()

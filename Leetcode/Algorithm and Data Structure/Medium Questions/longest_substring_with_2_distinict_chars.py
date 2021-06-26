"""
My Solution
"""
def lengthOfLongestSubstringTwoDistinct(s):
    n = len(s)
    left,right = 0,0
    hashmap = dict()
    maxLen = 2

    if n < 3:
        return n

    while right < n:
        hashmap[s[right]] = right
        right += 1

        if len(hashmap) == 3:
            del_idx = min(hashmap.values())
            del hashmap[s[del_idx]]
            left = del_idx + 1

        maxLen = max(maxLen, right-left)
    return maxLen

s = "eceba"
lengthOfLongestSubstringTwoDistinct(s)

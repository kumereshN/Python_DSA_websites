def lengthOfLongestSubstring(s):
    n = len(s)
    ans = i = 0
    # mp stores the current index of a character, to keep track of the index of the characters
    mp = {}
    
    # try to extend the range [i, j]
    for j in range(n): # j is the pointer that moves until it reaches a character that is similar to s[j], which is s[j] == s[i].
        if s[j] in mp: # If the character exists in the hash map, which is the repeating character.
            i = max(mp[s[j]], i) # Compare the index of the repeating character in the hash map against the index i and set the maximum value for i.

        ans = max(ans, j - i + 1) # Gets the maximum between ans and j - i + 1, which is the length of the string
        mp[s[j]] = j + 1

    return ans

s = "abcabcbb"
lengthOfLongestSubstring(s)

"""
i is the index of the repeating character. It acts as an anchor (e.g:j-i+1) j constantly moves while i remains in the same index until a repeating character comes along.
"""


# Alternative

def lengthOfLongestSubstring(s):
    dicts = {}
    maxlength = start = 0
    for i,value in enumerate(s):
        if value in dicts: # If the character in the dictionary
            sums = dicts[value] + 1
            if sums > start:
                start = sums
        num = i - start + 1
        if num > maxlength:
            maxlength = num
        dicts[value] = i
    return maxlength

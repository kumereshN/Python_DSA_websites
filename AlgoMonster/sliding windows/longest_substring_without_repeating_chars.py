def longest_substring_without_repeating_characters(s: str) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    res = 0
    seen = dict()
    left = 0
    
    for right, ch in enumerate(s):
        if ch in seen:
            # we want to get the max position of the left pointer
            left = max(left, seen[ch]+1)
        res = max(res, right - left + 1)
        seen[ch] = right
    return res
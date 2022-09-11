from collections import defaultdict

def characterReplacement(s: str, k: int) -> int:
    """
    Find largest window with >= N-k of the most abundant character
    * Time: O(N), Space: O(min(N, C)), C = variety of characters
    """
    d = defaultdict(lambda: 0) # frequency for each character
    start = 0   # first element of window
    end = -1	# for empty string case
    max_count = 0	# so we don't have to repeatedly calculate max(d.values())
    for end, ch in enumerate(s): # for each right-bound of window
        d[ch] += 1
        max_count = max(max_count, d[ch]) # get current max count. same value as max(d.values())
        res = end-start+1
        if max_count < res-k: # if the window as-is is invalid (has too many minority chars)
            d[s[start]] -= 1
            start += 1 # contract the window back, moving left-bound of window
    return end - start + 1    # we can simply do this, since it's the max window size reached at /any/ point in our loop
from collections import Counter


def checkInclusion(s1, s2):
    """
    Create a window of size s1.
    Check s2 if occurances of characters is same between s1 and s2 by sliding window from 0 to len(s2) - window_size.
    """
    window = len(s1)
    s1_c = Counter(s1)

    # Has to be the same size as s1
    for i in range(len(s2)-window+1):
        s2_c = Counter(s2[i:i+window])
        if s2_c == s1_c:
            return True

    return False

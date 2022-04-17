from collections import Counter

def get_minimum_window(original: str, check: str) -> str:
    # WRITE YOUR BRILLIANT CODE HERE
    need, missing = Counter(check), len(check)
    left = prev_start = prev_end = 0
    res = []
    # Right starts from 1, left is 0, so it'll be original[left:right] that will be appended to res.
    for right, c in enumerate(original, 1):
        if need[c] > 0:
            missing -= 1
        # This will include characters that are not found in need, like 'd' and it becomes 'd': -1
        need[c] -= 1
        if missing == 0:
            # as we move the right pointer, if we've found a repeating char, like 'c', we do the contraction of the window
            # so, it'll continue to move the left pointer until we've found another repeating char, like 'b', then we stop the while loop
            while left < right and need[original[left]] < 0:
                need[original[left]] += 1
                left += 1
            if not prev_end or right - left <= prev_end - prev_start:
                prev_start, prev_end = left, right
                res.append(original[prev_start:prev_end])

    res.sort()
    return res[0] if res else ""
    
original = 'cdbaebaecd'
check = 'abc'

get_minimum_window(original, check)

"""
Source: https://leetcode.com/problems/minimum-window-substring/discuss/26804/12-lines-Python
"""


def get_minimum_window(original: str, check: str) -> str:
    """ 
    First part: the right pointer keeps moving to the right until it finds all the chars in "need" matching a substring
    Second part: Moves the left pointer to remove duplicate and unwanted chars in the substring

    """
    # WRITE YOUR BRILLIANT CODE HERE
    need = Counter(check)  # hash table to store char frequency
    missing = len(check)  # total number of chars we care
    start, end = 0, 0
    left = 0
    res = []
    for right, char in enumerate(original, 1):  # index right from 1
        # If we've found a character in the string, decrement the number of missing characters in missing
        if need[char] > 0:
            missing -= 1
        # Decrement the character in need
        need[char] -= 1
        # Keep doing this until the substring matches all the characters in check
        if missing == 0:  # match all chars
            # Moves the left pointer to the right
            # The need[original[left]] < 0 is done until the need set is no longer contained by the check
            # remove chars to find the real start
            while left < right and need[original[left]] < 0:
                need[original[left]] += 1
                left += 1
            # make sure the first appearing char satisfies need[char]>0
            need[original[left]] += 1
            missing += 1  # we missed this first char, so add missing by 1
            # end - start is the len of the minimum substring that has been found up till now, we're comparing it against right-left which is the current len of the substring
            # the goal is to find the minimum substring
            if end == 0 or right-left <= end-start:  # update window
                # update the index of the minimum substring
                start, end = left, right
                res.append(original[start:end])
            # We move on to the next window, we move the left pointer
            left += 1  # update left to start+1 for next window
    res = sorted(res)
    return res[0] if res else ""


original = "cdbaebaecd"
check = "abc"

get_minimum_window(original, check)


def get_minimum_window(original: str, check: str) -> str:
    # WRITE YOUR BRILLIANT CODE HERE
    """
    My solution, not completed yet. Considers duplicates.
    """
    # Define variables
    n = len(original)
    to_check = set(check)
    window = set()
    l, r = 0, 0
    
    res = []
    
    while r <= n-1:                        
        # Find valid window
        window.add(original[r])
        r += 1
        check_if_contain = window.intersection(to_check)
        if check_if_contain != to_check:
            continue
            
        # Minimize the window
        while l < r:
            window.remove(original[l])
            l += 1
            check_if_contain = window.intersection(to_check)
            if check_if_contain == to_check:
                continue
            res.append(original[l-1:r])
            break
                    
        
    # Return result
    if not res:
        return ""        
    return min(res, key=len)
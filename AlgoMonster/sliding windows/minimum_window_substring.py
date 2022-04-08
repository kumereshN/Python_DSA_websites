from collections import Counter


def minWindow(s: str, t: str) -> str:
    """
    My advice for solving this problem is to:
    Understand the intuition and what to do at a high level
    Try to implement your own solution WITHOUT copying anyone elses
    This is how you will learn
    You will remember high level concepts, but never line for line code

    Intuition:
    Two pointers, left and right
    Both start from 0,0
    Increase right pointer until valid window is found
    Decrease left pointer until window is no longer valid
    Add the minimum length window you've found to your results
    Continue increasing right pointer, pretty much repeating what we did above
    Return the minimum length of your results
    """

    # Define variables
    s_count, t_count = Counter(s), Counter(t)

    l, r = 0, 0

    results = []

    while r <= len(s)-1:

        # Find valid window
        s_count[s[r]] += 1
        r += 1
        # '&' is the bitwise operator, sums both s_count and t_count, checks if t_count exists in s_count
        if s_count & t_count != t_count:
            continue

        # Minimize this window
        while l < r:
            s_count[s[l]] -= 1
            l += 1
            if s_count & t_count == t_count:
                continue
            results.append(s[l-1:r])
            break

    # Return result
    if not results:
        return ""
    return min(results, key=len)


""" Source: https://leetcode.com/problems/minimum-window-substring/discuss/1045266/Python-or-My-advice """


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

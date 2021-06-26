def isPalindrome(s):
    left, right = 0, len(s) - 1
    s = s.lower()

    # Loop to get only the alphanumeric characters (No punctuations)
    while left < right:
        while left < right and not s[left].isalnum(): # Check the left side if it's alphanumeric, if not increment by 1 on the left side
            left += 1
        while left < right and not s[right].isalnum(): # Check the right side if it's alphanumeric, if not increment by 1 on the right side
            right -= 1

        if s[left]!= s[right]:
            return False

        left += 1
        right -= 1

    return True

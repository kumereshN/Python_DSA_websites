def validPalindrome(s):
    def is_valid(left, right, s, delete=1):
        while left < right:
            if s[left] != s[right]:
                return (
                    is_valid(left + 1, right, s, delete - 1) or is_valid(left, right - 1, s, delete - 1)
                    if delete
                    else False
                )
            left, right = left + 1, right - 1
        return True

    return is_valid(0, len(s) - 1, s)


validPalindrome("abca")


# Alternative


def validPalindrome(s):
    # start scanning from both ends
    # you can skip at most 1 char

    if not s:
        return True

    start = 0
    end = len(s) - 1

    def isValid(start, end, skipped):
        if skipped > 1:
            return False

        if start >= end:
            return True

        if s[start] == s[end]:
            return isValid(start + 1, end - 1, skipped)
        else:
            return isValid(start, end - 1, skipped + 1) or isValid(start + 1, end, skipped + 1)

    return isValid(start, end, 0)


validPalindrome("abca")

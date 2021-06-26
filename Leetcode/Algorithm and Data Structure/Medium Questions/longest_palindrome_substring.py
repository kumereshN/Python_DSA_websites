def longestPalindrome(s):
    res = ""
    length = len(s)
    def helper(left: int, right: int):
        while left >= 0 and right < length and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1 : right]


    for index in range(length):
        res = max(helper(index, index), helper(index, index + 1), res, key = len) # get the max by length

    return res

s = "babad"
longestPalindrome(s)

# 1) Initialise the res to hold the string
# 2) Get the length of the current string
# 3) Create a helper function, with the criteria:
# 3a) As long as left >= 0 and right < len(s) and s[left] == s[right]
# 3b) Decrement the left by 1 and increment the right by 1
# 3c)  Break out of the loop and return s[left + 1 : right], which is the Palindrome string
# 4) Compares against the 2 helpers and the current res by the length and set it as the max for res



# First loop through the helper function
# Return the character "b"
# Second loop through the helper function
# Return the character ""
# Returns the character "b" comparing against "" and "" and output which is the maximum length: "b"

# Second loop through the helper function
# Return the character "bab"
# Second loop through the helper function
# Return the character ""
# Returns the character "bab" comparing against "b" and "" and output which is the maximum length among them: "bab"

# Third loop through the helper function
# Return the character "aba"
# Second loop through the helper function
# Return the character ""
# Returns the character "aba" comparing against "bab" and "" and output which is the maximum length among them: "aba"


# Alternative
def longestPalindrome(s):
    m = ''  # Memory to remember a palindrome
    for i in range(len(s)):  # i = start, O = n
        for j in range(len(s), i, -1):  # j = end, O = n^2
            if len(m) >= j-i:  # To reduce time, # Found the longest Palindrome string
                break
            elif s[i:j] == s[i:j][::-1]:
                m = s[i:j]
                break
    return m


# Alternative
class Solution:
    def longestPalindrome(self, s: str) -> str:
        p = ''
        for i in range(len(s)):
            p1 = self.get_palindrome(s, i, i+1)
            p2 = self.get_palindrome(s, i, i)
            p = max([p, p1, p2], key=lambda x: len(x))
        return p

    def get_palindrome(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

"""
Comments:
See it has used centre expansion technique. The expand around centre approach - we take one character from the centre and
then check that the preceding(L) and the exceeding(R) characters are equal or not. If they are equal, then we know that the string from L to R is a palindrome.
This approach has been discussed in count Palindromic substrings question. I would recommend you to attempt it.
The extra that is done in this question is that we have stored the strings from the L to R in a temp variable. We keep on updating the variable based on the length of the upcoming string and the current string stored. It is quite basic stuff. And in the end we return the string.
"""

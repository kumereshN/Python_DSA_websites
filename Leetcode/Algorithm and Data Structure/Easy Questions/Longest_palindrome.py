"""
        Given a string s of lowercase letters, this program
        determines the longest palindromic substring. It starts
        at every possible center point of a palindrome within
        s and keeps expanding the substring until it finds the
        longest palindrome from that center point.

        :param s: string of lowercase letters
        :type s: str
        :return: longest palindromic substring within s
        :rtype: str
        """

        """
        Initialization/Base Cases
        - Save length of s in len_s.
        - Initialize longest palindrome to empty string
        - Return quickly if s is empty or s is a palindrome.
        """
        len_s = len(s)
        longest_palindrome = ""
        if len_s == 0:
            return ""
        if s == s[::-1]:
            return s

        """
        Odd-Length Palindromes:
        - Start with a palindrome of length 1 at each location
          in s. This location becomes the center of the longest
          palindrome found from this location.
        - Expand in both directions until the longest palindrome
          is found.
        """
        for k in range(len_s):
            start = k
            end = k
            while start > 0 and end < len_s-1 and s[start-1] == s[end+1]: # start and end are the length of s
                start -= 1
                end += 1
            new_palindrome = s[start:end+1]
            if len(new_palindrome) > len(longest_palindrome):
                longest_palindrome = new_palindrome

        """
        Even-Length Palindromes:
        - start with palindrome of length 0 at each location
          that is between two letters in s.
        - Expand in both directions until the longest palindrome
          is found.
        """
        for k in range(len_s-1):
            start = k
            end = k + 1
            while start >= 0 and end < len_s and s[start] == s[end]:
                start -= 1
                end += 1
            new_palindrome = s[start+1:end]
            if len(new_palindrome) > len(longest_palindrome):
                longest_palindrome = new_palindrome

        return longest_palindrome

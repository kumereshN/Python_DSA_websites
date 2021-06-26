"""
Explanation:

This method uses an expand around center approach. The program iterates through each central point of a potential palindrome. moving left to right in the original input string.
It then expands outward (left and right) from the center point and checks if the two characters match.
This is done by moving a to the left by one and moving b to the right by one.
It keeps doing this until they don't match (i.e. s[a] == s[b] fails to be true) or either end of the input string is reached.
This expansion of the palindrome from its center outward occurs inside of the while loop.
Once the while loop exits, we have expanded as far as we could and the length of the palindrome is equal to (b - a - 1).
It is useful at this point to find the pattern between the length of a palindrome and the number of palindromes it contains (with the same center).
Notice the following pattern:

Palindromes of length 1 and 2 contain 1 palindrome:
a and aa each contain one palindrome with the same center: a contains itself and aa contains itself
Palindromes of length 3 and 4 contain 2 palindromes:
aba and abba each contain two palindromes with the same center: aba contains b and itself and abba contains bb and itself
Palindromes of length 5 and 6 contain 3 palindromes:
abcba and abccba each contain three palindromes with the same center: abcba contains c, bcb, and itself and abccba contains cc, bccb, and itself
etc. ...
The reason we are only counting palindromes with the same center and not other palindromes it may contain, is because we will have already counted them earlier in the for loop or will encounter them later in the for loop.
It is important that we do not double count.
Reflecting at the pattern above we can easily see that a palindrome of length n will contain (n+1)//2 palindromes within it that have the same center.
Since the length of our palindrome is (b - a - 1), it follows that the number of palindromes withint it will be (b - a)//2.
Thus at the end of the while loop, we add (b-a)//2 to count which is counting the total number of palindromes found thus far.

Perhaps the most important (and most challenging) part of the program occurs in the structure of the inner for loop: for a,b in [(i,i),(i,i+1)] This part may take a little explanation to fully understand.
A palindrome can be centered in one of two places.
The palindrome dad is centered on one of its letters, specifcally the letter a. If you had to pick two indices to describe where the palindrome dad is centered you would say that it was centered at the indices 1 and 1, since 1 is the index of a.
In general such palindromes (palindromes with an odd number of elements) are centered at (i,i) for some index i.
The other type of palindrome, abba is centered in between two identical letters, specifcally it is centered between the letters b and b.
If you had to pick two indices to describe where the palindrome abba is centered you would say that it was centered at the indices 1 and 2, since 1 and 2 are the indices of the central two b's. In general such palindromes (palindromes with an even number of elements) are centered at (i,i+1) for some index i. To correctly look at all the palindrome substrings, for each index i in the for loop we have to consider both centeral pivoting points. This is why the inner for loop iterates through both (i,i) and (i,i+1).

The program ends by returning count, the final total count of palindromes found within the original string s.

Glossary of Variables:
n = length of original input string
count = total current count of palindromic substrings
left = number of units left of center of palindrome
right = number of units right of center of palindrome
"""

def countSubstrings(s):
    n, count = len(s), 0
    for i in range(n):
    	for left,right in [(i,i),(i,i+1)]: # Two cases: (i,i) and (i,i+1). Left and right are split inside the (i,i) and (i,i+1)
    		while left >= 0 and right < n and s[left] == s[right]:
                 left -= 1
                 right += 1
    		count += (right-left)//2
    return count

s = "abc"
countSubstrings(s)


- Junaid Mansuri
(LeetCode ID)@hotmail.com

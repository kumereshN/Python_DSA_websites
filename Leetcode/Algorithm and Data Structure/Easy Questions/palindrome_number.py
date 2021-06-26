# Link: https://leetcode.com/problems/palindrome-number/discuss/785314/Python-3-greater-1-solution-is-89.20-faster.-2nd-is-99.14-faster.-Explanation-added

def isPalindrome(x):
	if x < 0 or (x > 0 and x%10 == 0):   # if x is negative, return False. if x is positive and last digit is 0, that also cannot form a palindrome, return False.
		return False

	result = 0
	while x > result:
		result = result * 10 + x % 10 # x % 10 gets you the last digit of x
		x = x // 10 # Removes the last digit in the while loop

	return True if (x == result or x == result // 10) else False # the result // 10 removes the last number in the result if it's odd length

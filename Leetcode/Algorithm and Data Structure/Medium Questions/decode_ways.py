def numDecodings(s):
    dp = [1] * (len(s) + 1)             # DP Array of size (n+1) initialized to 1
    if s[0] == "0": dp[1] = 0           # Check s[0] is valid encoding

    for i in range(2, len(s) + 1):
        dp[i] = (dp[i - 1] if 1 <= int(s[i - 1]) <= 26 else 0) + (dp[i - 2] if 10 <= int(s[i - 2] + s[i - 1]) <= 26 else 0) # 1
    return dp[-1]





# 1: If the number in the i - 1 index is between 1 and 26, replace the number in the i index with the number in the i - 1 index.
# 2:




# Alternative
def numDecodings(s):
    dp = [0] * (len(s) + 1)
    dp[0],dp[1]=1,1
    if s[0] == "0":
        return 0
    for i in range(2, len(s) + 1):
        if 1 <= int(s[i-1]) <= 9: # If the first index number is between 1 and 9,
            dp[i] += dp[i - 1] # Add the second index number with the first index number
        if 10 <= int(s[i - 2] + s[i - 1]) <= 26: # If the first index number and second index number combined is between 10 and 26
            dp[i] += dp[i - 2] # Add the second index number with the first index number
    return dp[-1] # Return the last number

numDecodings("12")

# Now lets try to see it step by step:
#
# First we create a list dp, which we have initized to 0.
#
# Now, dp[i]==> This denotes the number of decodings possible upto [i-1]th element of s. In other words, to calculate decoding upto ith character of s, we need to know dp[i+1]. Hence , when we calculate dp[len(s)] or dp[-1] , it will give us the number of decodings till s[len(s)-1], hence the answer
#
# Now, try to understand this one:
# dp[i-1] ==> gives the number of decodings until [i-2] element of s in consideration , and since we are considering till s[i-1] ,hence only one letter can be placed at the end, resulting in new sequences. This is the number of sequences which are formed by using the last one character.
#
# dp[i-2]==>gives the number of decodings until [i-3] element of s in consideration , and since we are considering till s[i-1] ,hence two letters can be placed at the end, resulting in new sequences. This is the number of sequences which are formed by using the last two characters.
#
# Now the edge cases:
#
# If s[i-1]==0==> means that the last character cannot be used for making new decodings, as we dont have code for 0, hence we test this condition using
# if 1<=int(s[i-1])<=9
#
# If the last two digits in consideration add up to give more than 26, we have the same problem as before with having no code assigned to them and hence no decodings possible for this case either. We check this using
# if 10 <= int(s[i - 2] + s[i - 1]) <= 26
# After these two edge cases, all conditions have been acounted for and we simply return the result.

# Source : https://leetcode.com/problems/decode-ways/discuss/1029225/Simple-and-detail-solution-with-explanation

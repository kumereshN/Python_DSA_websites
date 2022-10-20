from collections import Counter

def characterReplacement(s: str, k: int) -> int:
    count = Counter()
    # res the longest subsequence without repeating chars and k changes
    # maxfreq is the high count chars in the answer subsequence
    maxfreq = res = 0
    n = len(s)
    
    for i in range(n):
         # Add char to the count dict
        count[s[i]] += 1
        # key idea(2): Find the new maxfreq. This is much like Kadane's
        # Where we only consider if the new length exceedes the res overall
        maxfreq = max(maxfreq, count[s[i]])
        if res - maxfreq < k:
            res += 1
        else:
            # key idea(3) This removes the char at the start of the subsequence s[i-res]
            # This serves as "correction" for the subsequence problem
            count[s[i - res]] -= 1
    return res


s = "ABAB"
k = 2

print(characterReplacement(s,k))
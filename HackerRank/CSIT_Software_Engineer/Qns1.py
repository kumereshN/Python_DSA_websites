"""
Fun with Anagrams

Use collections.Counter to verify if the second string is an Anagram of the first string

If it's an Anagram, remove the second str from text list

Sample cases:
text = ['code','aaagmnrs','anagrams','doce']
"""
def anagrams(text):
    ans = []
    N = len(text)

    found = dict()

    for i in range(N):
        word = " ".join(sorted(text[i]))

        if (word not in found):
            ans.append(text[i])
            found[word] = 1

    ans = sorted(ans)
    return ans

text = ['code','aaagmnrs','anagrams','doce']
anagrams(text)

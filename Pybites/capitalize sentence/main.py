from collections import Counter

def is_anagram(word1, word2):
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""
    word1 = Counter([s.lower() for s in word1 if s.isalnum()])
    word2 = Counter([s.lower() for s in word2 if s.isalnum()])
    return word1 == word2

word1, word2 = "roast beef", "eat for BSE"
print(is_anagram(word1, word2))

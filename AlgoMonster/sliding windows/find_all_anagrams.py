from typing import List

# word2 should be sorted already return sorted(word1) == word2
def find_all_anagrams(original: str, check: str):
    def is_anagram(word_one, word_two):
        word_one = ''.join(sorted(word_one))
        word_two = ''.join(sorted(word_two))
        return word_one == word_two
    
    left = 0
    right = len(check)
    res = []
    n = len(original)
    
    while right <= n:
        if is_anagram(original[left:right], check):
            res.append(left)
        left += 1
        right += 1
    return res

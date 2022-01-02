# word2 should be sorted already return sorted(word1) == word2
def find_all_anagrams(original: str, check: str) -> List[int]:
    def isAnagram(word1, word2):
        # word2 should be sorted already
        return sorted(word1) == word2

    left = 0
    right = len(check)
    res = []
    check = sorted(check)

    while right <= len(original):
        if isAnagram(original[left:right], check):
            res.append(left)

        right += 1
        left += 1

    return res

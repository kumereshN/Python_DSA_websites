from typing import List
from itertools import groupby

def group_anagrams(strings: List[str]) -> List[List[str]]:
    """Group anagrams together."""
    res = []
    sorted_words_tuple = sorted([(''.join(sorted(s)),s) for s in strings], key = lambda x: x[0])
    for _, string_group in groupby(sorted_words_tuple, key= lambda x: x[0]):
        group_of_words = [string[1] for string in string_group]
        res.append(group_of_words)
    return res


if __name__ == "__main__":
    lst = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(lst))
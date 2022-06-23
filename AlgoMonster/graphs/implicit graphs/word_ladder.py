from typing import List
from collections import deque
from string import ascii_lowercase

def word_ladder(begin: str, end: str, word_list: List[str]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    words = set(word_list) # make a set because existence query is O(1) vs O(N) for list
    q = deque([begin])
    steps = -1 # -1 to not count 'cold' which is the first word

    def get_next_word(word):
        res = []
        for i in range(len(word)):
            for c in ascii_lowercase:
                next_word = word[:i] + c + word[i+1:]
                res.append(next_word)
        return res
    
    while q:
        steps += 1
        n = len(q)
        for _ in range(n):
            word = q.popleft()
            if word == end:
                return steps
            if word not in words:
                continue
            q.extend(get_next_word(word))
            words.remove(word) # removing from the set is equivalent as marking the word visited
    return 0 

begin, end, word_list = "cold", "warm", ["cold", "gold", "cord", "sold", "card", "ward", "warm", "tard"]
print(word_ladder(begin, end, word_list))
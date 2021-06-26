class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # mapping of char to order: order = "hlabcdefgijkmnopqrstuvwxyz"
        if not words or len(words) <2:
            return True

        vocab = {v: k for k, v in enumerate(order)}

        word_index = [[vocab[char] for char in w] for w in words]

        for w1, w2 in zip(word_index, word_index[1:]):
            if w1 >= w2:
                return False
        return True


    def isAlienSorted2(self, words: List[str], order: str) -> bool: # Preferred solution
        """This is a more compact way"""
        vocab = {v: k for k, v in enumerate(order)}
        prev=[]
        for i in range(len(words)):
            word = [vocab[char] for char in words[i]]
            if word < prev: # We eliminate the 2nd pass at these words by checking previous. # My Notes: If the value of the second word is less than the first word, then it's not lexiconically sorted
                return False
            prev = word
        return True

# Source: https://leetcode.com/problems/verifying-an-alien-dictionary/discuss/1027313/python-with-explaination


# Alternative
def isAlienSorted(words, order):
        o = {c:i for i,c in enumerate(order)}
        return words == sorted(words, key=lambda s: [o[c] for c in s]) # Sort by the order dictionary which is o

isAlienSorted(["hello","leetcode"],"hlabcdefgijkmnopqrstuvwxyz")

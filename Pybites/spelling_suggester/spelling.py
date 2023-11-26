from difflib import SequenceMatcher
import os
from typing import Union
from urllib.request import urlretrieve
# Remove later
import string

TMP = os.getenv("TMP", "/tmp")
DICTIONARY = os.path.join(TMP, 'dictionary.txt')
if not os.path.isfile(DICTIONARY):
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/dictionary.txt',
        DICTIONARY
    )


def load_words():
    'return dict of words in DICTIONARY'
    with open(DICTIONARY) as f:
        return {word.strip().lower() for word in f.readlines() \
                if word.startswith('a') and len(word) > 1 \
                and word[1] in string.ascii_letters[:13]}


def suggest_word(misspelled_word: str, words: Union[set, None]) -> str:
    """Return a valid alternative word that best matches
       the entered misspelled word"""
    if words is None:
        words = load_words()

    seq = SequenceMatcher()
    seq.set_seq2(misspelled_word)

    res = dict()
    
    for word in words:
        seq.set_seq1(word)
        ratio = seq.quick_ratio()
        res[word] = ratio
    
    best_match = max(res, key = res.get)
    return best_match


# print(suggest_word('acheive', load_words()))
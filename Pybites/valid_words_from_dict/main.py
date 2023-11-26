from itertools import permutations
import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DICT}',
    DICTIONARY
)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    permutation_set = _get_permutations_draw(draw)
    return [word for word in permutation_set if word in dictionary]

def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    draw = tuple(map(str.lower, draw))

    for i in range(1, len(draw)+1):
        letter_groups = permutations(draw, r=i)
        yield from (''.join(group) for group in letter_groups)


word_1 = 'T, I, I, G, T, T, L'
word_2 = 'O, N, V, R, A, Z, H'

draw_1 = list(w.lower() for w in word_1.split(', '))
draw_2 = list(w.lower() for w in word_2.split(', '))

# print('zonar' in dictionary)
print(get_possible_dict_words(draw_2))
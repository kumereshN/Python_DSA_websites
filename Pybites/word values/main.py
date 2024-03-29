import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(f'{S3}{DICT}', DICTIONARY)

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}

# start coding

def load_words():
    """Load the words dictionary (DICTIONARY constant) into a list and return it"""
    with open(DICTIONARY, 'r') as f:
        return [x.strip() for x in f]


def calc_word_value(word):
    """Given a word calculate its value using the LETTER_SCORES dict"""
    ch_lst = [LETTER_SCORES.get(c.upper(), 0) for c in word]
    return sum(ch_lst)




def max_word_value(words):
    """Given a list of words calculate the word with the maximum value and return it"""
    words_scores_dict =  {w: calc_word_value(w) for w in words}
    return max(words_scores_dict, key= words_scores_dict.get)


print(max_word_value(['bob', 'julian', 'pybites', 'quit', 'barbeque']))
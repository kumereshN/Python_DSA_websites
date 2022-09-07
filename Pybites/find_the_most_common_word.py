import os
import urllib.request

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)


def get_harry_most_common_word():
    
    def clean_words(lst, stop_words):
        final_word_lst = []
        for word in lst:
            clean_char_lst = []
            if word not in stop_words and word != '':
                for letter in word:
                    if letter.isalnum():
                        clean_char_lst.append(letter.lower())
                final_word_lst.append("".join(clean_char_lst))
        return final_word_lst
    
    stopwords_set = set()
    with open(stopwords_file) as f:
        for line in f:
            stopwords_set.add(line.strip())
    
    words_lst = []
    
    with open(harry_text, 'rb') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if not line:
                continue
            words_lst.extend(clean_words(line.split(), stopwords_set))
            
    print(words_lst)
        

get_harry_most_common_word()
        
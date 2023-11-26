import requests
import json
import re

URL = 'https://bites-data.s3.us-east-2.amazonaws.com/omdb_data'
resp = requests.get(URL)

if resp.status_code == 200:
    movie_lst = resp.text.strip().split('\n')
    dict_lst = [json.loads(x) for x in movie_lst]

    sample_movie = dict_lst[0]
    comedy_movies = [m.get('Title', 'No movies with comedy') for m in dict_lst if 'Comedy' in m.get('Genre', '')].pop()

    nomination_number_pattern = '(\d+) nominations.*'
    
    movies_with_nomination = [(m.get('Title', None),int(re.findall(nomination_number_pattern,m.get('Awards', None))[0])) for m in dict_lst if 'nomination' in m.get('Awards', None) or 'nominations' in m.get('Awards', None)]
    
    movie_with_most_nomination = max(movies_with_nomination, key=lambda x: x[1])[0]

    movies_runtime = [(m.get('Title', None), int(m.get('Runtime', None).split(' ')[0])) for m in dict_lst]

    movie_with_longest_runtime = max(movies_runtime, key = lambda x: x[1])[0]

    print(movie_with_longest_runtime)

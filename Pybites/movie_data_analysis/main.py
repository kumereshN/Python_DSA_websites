import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = os.getenv("TMP", "/tmp")

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    res = defaultdict(list)

    with open(MOVIE_DATA, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            director_name, movie_title, title_year, imdb_score = row.get('director_name', False), row.get('movie_title', False), row.get('title_year', False), row.get('imdb_score', False)
            if all([director_name, movie_title, title_year, imdb_score]):
                title_year = int(title_year)
                imdb_score = float(imdb_score)
                if title_year > MIN_YEAR:
                    res[director_name].append(Movie(movie_title, title_year, imdb_score))
    return res
                



def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    imdb_scores_movies = [t.score for t in movies]
    return round(sum(imdb_scores_movies) / len(imdb_scores_movies),1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    direct_avg_score_tuple = [(director, calc_mean_score(l)) for director, l in directors.items() if len(l) >= MIN_MOVIES]
    return sorted(direct_avg_score_tuple, key = lambda x: x[1], reverse=True)


movies = get_movies_by_director()
print(get_average_scores(movies))
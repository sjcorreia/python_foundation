from __future__ import print_function
import media
import fresh_tomatoes
import json

moviesList = []

# https://docs.python.org/3/library/json.html

with open('json/movies.json') as json_data_movies:
    # Reading from a JSON file into a python dict, or list of dicts
    # https://www.json.org/
    data_movies = json.load(json_data_movies)

    for movie in data_movies["favoriteMovies"]:
        moviesList.append(media.Movie(movie["movieTitle"],
                                      movie["summary"],
                                      movie["posterLink"],
                                      movie["trailerLink"]))

fresh_tomatoes.open_movies_page(moviesList)

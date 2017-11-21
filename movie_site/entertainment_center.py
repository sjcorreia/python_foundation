from __future__ import print_function
import media
import fresh_tomatoes

ghostbusters = media.Movie("Ghostbusters", "Scientists save the world from the Paranormal, Who you gonna call?",
    "https://upload.wikimedia.org/wikipedia/en/2/2f/Ghostbusters_%281984%29_theatrical_poster.png",
    "https://www.youtube.com/watch?v=EQCCPP8aZBY")

the_last_jedi = media.Movie("Star Wars: The Last Jedi", "Rey continues her journey in connection with the Force",
    "https://upload.wikimedia.org/wikipedia/en/7/7f/Star_Wars_The_Last_Jedi.jpg",
    "https://www.youtube.com/watch?v=Q0CbN8sfihY")

raiders_of_the_lost_ark = media.Movie("Raiders of the Lost Ark", "Dr. Jones battles some Nazis to recover the Ark of the Convenant",
    "https://upload.wikimedia.org/wikipedia/en/4/4c/Raiders_of_the_Lost_Ark.jpg",
    "https://www.youtube.com/watch?v=XkkzKHCx154")

back_to_the_future = media.Movie("Back to the Future", "A son helps his father meet get with his mother",
    "https://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg",
    "https://www.youtube.com/watch?v=qvsgGtivCgs")

the_dark_knight = media.Movie("The Dark Knight", "Batman meets the Joker", 
    "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
    "https://www.youtube.com/watch?v=EXeTwQWrcwY")

casino_royale = media.Movie("Casino Royale", "James Bond becomes  007",
    "https://upload.wikimedia.org/wikipedia/en/1/15/Casino_Royale_2_-_UK_cinema_poster.jpg",
    "https://www.youtube.com/watch?v=36mnx8dBbGE")

the_other_guys = media.Movie("The Other Guys", "A different kind of buddy cop movie",
    "https://upload.wikimedia.org/wikipedia/en/6/6b/Other_guys_poster.jpg",
    "https://www.youtube.com/watch?v=D6WOoUG1eNo")

# print(ghostbusters.storyline)
# print(the_last_jedi.storyline)
# the_last_jedi.show_trailer()
# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)

movies = [ghostbusters, the_last_jedi, raiders_of_the_lost_ark, back_to_the_future, the_dark_knight, the_other_guys]
fresh_tomatoes.open_movies_page(movies)
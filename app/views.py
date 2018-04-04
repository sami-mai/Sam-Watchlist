from flask import render_template
from app import app
# from .request import get_movies

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    message = 'Hi World!'
    # print("hhhhh")
    # return render_template('index.html',message = message)

    # Getting popular movie
    # popular_movies = get_movies('popular')
    # print(popular_movies)
    # adding more categories
    # upcoming_movie = get_movies('upcoming')
    # now_showing_movie = get_movies('now_playing')

    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title, message = message) #, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie)

# add a new route that have a movie() view function.
# The part in the angle brackets <> is dynamic.

# @app.route('/movie/<movie_id>')

# changed the dynamic part to <int:movie_id> to transform content to integer.
@app.route('/movie/<int:movie_id>')
def movie(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('movie.html',id = movie_id)

from flask_app import app
from flask import redirect, render_template,request
from flask_app.models.filmmaker_model import Filmmaker
from flask_app.models.movie_model import Movie

@app.route('/movies')
def movies():
    return render_template('movies.html',all_movies=Movie.get_all(),all_filmmakers=Filmmaker.get_all())
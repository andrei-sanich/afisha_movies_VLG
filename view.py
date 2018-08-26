from app import app
from flask import render_template, request, json

from models import Movie
from parse_list import parse_list


@app.route('/')
def index():
    list_genres = [row[0] for row in Movie.query.with_entities(Movie.genres)]
    genres = set()
    for genre in list_genres:
        temp = [g for g in parse_list(genre)]
        genres.update(temp)
    
    return render_template('index.html', genres=sorted(genres))


@app.route('/get_movies', methods=['GET', 'POST'])
def get_movies():
    genres = request.form.getlist('genres')
    all_movies = Movie.query.all()
    find_movies = [movie for movie in all_movies if set(genres).issubset(set(parse_list(movie.genres)))]
    result = [res.to_json() for res in find_movies]
    return json.dumps({'movies': result})


@app.route('/analytics')
def analytics():
    return render_template('analytics.html')
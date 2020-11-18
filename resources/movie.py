from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.movie import Movie, movie_list


class MovieListResource(Resource):

    def get(self):

        data = []

        for movie in movie_list:
            data.append(movie.data)

        return {'data': data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()

        movie = Movie(name=data['name'],
                      year=data['year'],
                      rating=data['rating'],
                      description=data['description'],
                      director=data['director'],
                      duration=data['duration'],
                      age_rating=data['age_rating'])

        movie_list.append(movie)

        return movie.data, HTTPStatus.CREATED


class MovieResource(Resource):

    def get(self, movie_id):
        movie = next((movie for movie in movie_list if movie.id == movie_id), None)

        if movie is None:
            return {'message': 'movie not found'}, HTTPStatus.NOT_FOUND

        return movie.data, HTTPStatus.OK

    def put(self, movie_id):
        data = request.get_json()

        movie = next((movie for movie in movie_list if movie.id == movie_id), None)

        if movie is None:
            return {'message': 'movie not found'}, HTTPStatus.NOT_FOUND

        movie.name = data['name']
        movie.year = data['year']
        movie.rating = data['rating']
        movie.description = data['description']
        movie.director = data['director']
        movie.duration = data['duration']
        movie.age_rating = data['age_rating']

        return movie.data, HTTPStatus.OK

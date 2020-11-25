from flask import request
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required
from http import HTTPStatus

from models.movie import Movie
from models.user import User


class MovieListResource(Resource):

    # for getting all movies, accessible by all
    def get(self):

        movies = Movie.get_all_movies()

        data = []

        for movie in movies:
            data.append(movie.data())

        return {'data': data}, HTTPStatus.OK

    # for adding a movie, only admin
    @jwt_required
    def post(self):

        json_data = request.get_json()

        identity = get_jwt_identity()
        current_user = User.get_by_id(identity)

        if not current_user.is_admin:
            return {'message': 'Not authorized'}, HTTPStatus.UNAUTHORIZED

        movie = Movie(name=json_data['name'],
                      year=json_data['year'],
                      rating=json_data['rating'],
                      description=json_data['description'],
                      director=json_data['director'],
                      duration=json_data['duration'],
                      age_rating=json_data['age_rating'])

        movie.save()

        return movie.data(), HTTPStatus.CREATED


class MovieResource(Resource):

    # for getting a specific movie, accessible by all
    def get(self, movie_id):

        movie = Movie.get_by_id(movie_id=movie_id)

        if movie is None:
            return {'message': 'movie not found'}, HTTPStatus.NOT_FOUND

        return movie.data(), HTTPStatus.OK

    # for updating movie, only admin
    @jwt_required
    def put(self, movie_id):

        json_data = request.get_json()

        movie = Movie.get_by_id(movie_id=movie_id)

        if movie is None:
            return {'message': 'movie not found'}, HTTPStatus.NOT_FOUND

        identity = get_jwt_identity()
        current_user = User.get_by_id(identity)

        if not current_user.is_admin:
            return {'message': 'Not authorized'}, HTTPStatus.UNAUTHORIZED

        movie.name = json_data['name']
        movie.year = json_data['year']
        movie.rating = json_data['rating']
        movie.description = json_data['description']
        movie.director = json_data['director']
        movie.duration = json_data['duration']
        movie.age_rating = json_data['age_rating']

        movie.save()

        return movie.data(), HTTPStatus.OK

    # for deleting a movie, only admin
    @jwt_required
    def delete(self, movie_id):

        movie = Movie.get_by_id(movie_id=movie_id)

        if movie is None:
            return {'message': 'movie not found'}, HTTPStatus.NOT_FOUND

        identity = get_jwt_identity()
        current_user = User.get_by_id(identity)

        if not current_user.is_admin:
            return {'message': 'Not authorized'}, HTTPStatus.UNAUTHORIZED

        movie.delete()

        return {'message': 'deleted successfully!'}, HTTPStatus.OK

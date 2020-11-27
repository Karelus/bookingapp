from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from Config import Config
from extensions import db, jwt
from resources.user import UserListResource, UserResource, MeResource, AdminResource
from resources.review import ReviewListResource, ReviewResource, ReviewPublishResource, ReviewResourceByMovie
from resources.movie import MovieListResource, MovieResource, MovieRatingResource
from resources.token import TokenResource


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_resources(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)
    jwt.init_app(app)


def register_resources(app):
    api = Api(app)

    api.add_resource(UserListResource, '/users')
    api.add_resource(UserResource, '/users/<string:username>')
    api.add_resource(MeResource, '/me')
    api.add_resource(TokenResource, '/token')
    api.add_resource(AdminResource, '/admin')

    api.add_resource(ReviewListResource, '/reviews')
    api.add_resource(ReviewResource, '/reviews/<int:review_id>')
    api.add_resource(ReviewPublishResource, '/reviews/<int:review_id>/publish')
    api.add_resource(ReviewResourceByMovie, '/reviews/bymovie/<int:movie_id>')

    api.add_resource(MovieListResource, '/movies')
    api.add_resource(MovieResource, '/movies/<int:movie_id>')
    api.add_resource(MovieRatingResource, '/ratings/<int:movie_id>')


if __name__ == "__main__":
    app = create_app()
    app.run()



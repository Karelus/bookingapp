from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from Config import Config
from extensions import db
from resources.user import UserListResource
from resources.review import ReviewListResource, ReviewResource, ReviewPublishResource
from resources.movie import MovieListResource, MovieResource


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_resources(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)


def register_resources(app):
    api = Api(app)

    api.add_resource(UserListResource, '/users')

    api.add_resource(ReviewListResource, '/reviews')
    api.add_resource(ReviewResource, '/reviews/<int:review_id>')
    api.add_resource(ReviewPublishResource, '/reviews/<int:review_id>/publish')

    api.add_resource(MovieListResource, '/movies')
    api.add_resource(MovieResource, '/movies/<int:movie_id>')


reviews = [
    {
        'id': 1,
        'author': 'Karel',
        'content': 'This was a very good movie.'
    },
    {
        'id': 2,
        'author': 'Kappe',
        'content': 'Not that good tbh.'
    }
]

movies = [
    {
        'id': 1,
        'name': 'Matrix',
        'description': 'Guy takes a red pill.'
    },
    {
        'id': 2,
        'name': 'Fight Club',
        'description': 'Guy establishes an underground fight club.'
    }
]


if __name__ == "__main__":
    app = create_app()
    app.run()



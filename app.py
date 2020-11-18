from flask import Flask
from flask_restful import Api

from resources.review import ReviewListResource, ReviewResource, ReviewPublishResource
from resources.movie import MovieListResource, MovieResource


app = Flask(__name__)
api = Api(app)

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

api.add_resource(ReviewListResource, '/reviews')
api.add_resource(ReviewResource, '/reviews/<int:review_id>')
api.add_resource(ReviewPublishResource, '/reviews/<int:review_id>/publish')

api.add_resource(MovieListResource, '/movies')
api.add_resource(MovieResource, '/movies/<int:movie_id>')


if __name__ == "__main__":
    app.run(port=5000, debug=True)

"""
# get methods
@app.route('/reviews', methods=['GET'])
def get_reviews():
    return jsonify({'data': reviews})


@app.route('/reviews/<int:review_id>', methods=['GET'])
def get_review(review_id):
    review = next((review for review in reviews if review['id'] == review_id), None)

    if review:
        return jsonify(review)

    return jsonify({'message': 'review not found'}), HTTPStatus.NOT_FOUND


@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify({'data': movies})


@app.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = next((movie for movie in movies if movie['id'] == movie_id), None)

    if movie:
        return jsonify(movie)

    return jsonify({'message': 'movie not found'}), HTTPStatus.NOT_FOUND


# post methods
@app.route('/reviews', methods=['POST'])
def create_review():
    data = request.get_json()

    author = data.get('author')
    content = data.get('content')

    review = {
        'id': len(reviews) + 1,
        'author': author,
        'content': content
    }

    reviews.append(review)

    return jsonify(review), HTTPStatus.CREATED


# put methods
@app.route('/reviews/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    review = next((review for review in reviews if review['id'] == review_id), None)

    if not review:
        return jsonify({'message': 'review not found'}), HTTPStatus.NOT_FOUND

    data = request.get_json()

    review.update(
        {
            'author': data.get('author'),
            'content': data.get('content')
        }
    )

    return jsonify(review)
"""

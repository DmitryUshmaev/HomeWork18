# Создание пространства имен для movie и работа с запросами к таблице movie

from flask_restx import Resource, Namespace
from flask import request

from implemented import movie_service
from dao.model.movie import MovieSchema

# Создание пространства имен для movie
movie_ns = Namespace('movies')

# Создание схемы объекта movie
movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


@movie_ns.route('/')
class MoviesView(Resource):

    def get(self):
        all_movies = movie_service.get_all_movies()
        director_id = request.args.get('director_id')
        movie_year = request.args.get('year')
        genre_id = request.args.get('genre_id')

        if director_id is not None:
            all_movies = movie_service.get_movies_by_director(director_id)
        elif movie_year is not None:
            all_movies = movie_service.get_movie_by_year(movie_year)
        elif genre_id is not None:
            all_movies = movie_service.get_movies_by_genre(genre_id)

        movies = all_movies

        return movies_schema.dump(movies), 200

    def post(self):
        req_json = request.json

        movie_service.create_movie(req_json)

        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):

    def get(self, mid):
        try:
            movie = movie_service.get_one_movie(mid)
            return movie_schema.dump(movie), 200
        except Exception as e:
            return '', 404

    def put(self, mid):
        req_json = request.json
        req_json['id'] = mid

        movie_service.update_movie(req_json)

        return "", 204

    def delete(self, mid):
        movie_service.delete_movie(mid)

        return "", 204

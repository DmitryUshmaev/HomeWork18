# Создание пространства имен для genre и работа с запросами к таблице genre

from flask_restx import Resource, Namespace

from implemented import genre_service
from dao.model.genre import GenreSchema

# Создание пространства имен для genre
genre_ns = Namespace('genres')

# Создание схемы объекта genre
genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()


@genre_ns.route('/')
class GenreView(Resource):

    def get(self):
        genres = genre_service.get_all_genres()

        return genres_schema.dump(genres), 200


@genre_ns.route('/<int:gid>')
class DirectorView(Resource):

    def get(self, gid):
        try:
            genre = genre_service.get_one_genre(gid)
            return genre_schema.dump(genre), 200
        except Exception as e:
            return '', 404

# Создание пространства имен для director и работа с запросами к таблице director

from flask_restx import Resource, Namespace

from implemented import director_service
from dao.model.director import DirectorSchema

# Создание пространства имен для director
director_ns = Namespace('directors')

# Создание схемы объекта movie
directors_schema = DirectorSchema(many=True)
director_schema = DirectorSchema()


@director_ns.route('/')
class DirectorView(Resource):

    def get(self):
        directors = director_service.get_all_directors()

        return directors_schema.dump(directors), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):

    def get(self, did):
        try:
            director = director_service.get_one_director(did)
            return director_schema.dump(director), 200
        except Exception as e:
            return '', 404

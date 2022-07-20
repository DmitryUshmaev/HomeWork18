# файл для создания DAO и сервисов чтобы импортировать их везде
from setup_db import db

from dao.movie import MovieDAO
from service.movie import MovieService

from dao.director import DirectorDAO
from service.director import DirectorService

from dao.genre import GenreDAO
from service.genre import GenreService

# Объекты DAO и Service movie

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

# Объекты DAO и Service director

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

# Объекты DAO и Service genre

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)


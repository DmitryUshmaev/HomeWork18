# DAO структура для работы с таблицей movie

from dao.model.movie import Movie


class MovieDAO:
    """Подключение сессии базы данных"""

    def __init__(self, session):
        self.session = session

    """Получение всех фильмов"""

    def get_all_movies(self):
        return self.session.query(Movie).all()

    """Получение одного фильма"""

    def get_one_movie(self, mid):
        return self.session.query(Movie).get(mid)

    """Создание фильма"""

    def create_movie(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie

    """Обновление фильма"""

    def update_movie(self, movie):
        self.session.add(movie)
        self.session.commit()

        return movie

    """Удаление фильма"""

    def delete_movie(self, mid):
        movie = self.session.query(Movie).get(mid)

        self.session.delete(movie)
        self.session.commit()

    """Получение фильмов по режиссеру"""

    def get_movies_by_director(self, did):
        movies = self.session.query(Movie).filter(Movie.director_id == did)

        return movies

    """Получение фильмов по жанру"""

    def get_movies_by_genre(self, gid):
        movies = self.session.query(Movie).filter(Movie.genre_id == gid)

        return movies

    """Получение фильмов по году выпуска"""

    def get_movie_by_year(self, year):
        movies = self.session.query(Movie).filter(Movie.year == year)

        return movies

# DAO структура для работы с таблицей genre

from dao.model.genre import Genre


class GenreDAO:

    """Подключение сессии базы данных"""

    def __init__(self, session):
        self.session = session

    """Получение всех фильмов"""

    def get_all_genres(self):
        return self.session.query(Genre).all()

    """Получение одного фильма"""

    def get_one_genre(self, gid):
        return self.session.query(Genre).get(gid)
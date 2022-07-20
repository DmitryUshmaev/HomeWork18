# DAO структура для работы с таблицей director

from dao.model.director import Director


class DirectorDAO:

    """Подключение сессии базы данных"""

    def __init__(self, session):
        self.session = session

    """Получение всех фильмов"""

    def get_all_directors(self):
        return self.session.query(Director).all()

    """Получение одного фильма"""

    def get_one_director(self, did):
        return self.session.query(Director).get(did)



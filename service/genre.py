from dao.model.genre import Genre


class GenreService:

    def __init__(self, dao: Genre):
        self.dao = dao

    def get_all_genres(self):
        return self.dao.get_all_genres()

    def get_one_genre(self, gid):
        return self.dao.get_one_genre(gid)
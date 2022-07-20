from dao.model.director import Director


class DirectorService:

    def __init__(self, dao: Director):
        self.dao = dao

    def get_all_directors(self):
        return self.dao.get_all_directors()

    def get_one_director(self, did):
        return self.dao.get_one_director(did)

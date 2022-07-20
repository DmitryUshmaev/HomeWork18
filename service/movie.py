from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all_movies(self):
        return self.dao.get_all_movies()

    def get_one_movie(self, mid):
        return self.dao.get_one_movie(mid)

    def create_movie(self, data):
        return self.dao.create_movie(data)

    def update_movie(self, data):
        mid = data.get('id')
        movie = self.get_one_movie(mid)

        movie.year = data.get('year')
        movie.trailer = data.get('trailer')
        movie.description = data.get('description')
        movie.title = data.get('title')

        self.dao.update_movie(movie)

    def delete_movie(self, mid):
        return self.dao.delete_movie(mid)

    def get_movies_by_director(self, mid):
        return self.dao.get_movies_by_director(mid)

    def get_movies_by_genre(self, gid):
        return self.dao.get_movies_by_genre(gid)

    def get_movie_by_year(self, year):
        return self.dao.get_movie_by_year(year)


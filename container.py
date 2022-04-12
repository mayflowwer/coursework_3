from project.dao import GenreDAO
from project.dao.director import DirectorDAO
from project.dao.movie import MovieDAO
from project.dao.user import UserDAO
from project.services.directors_service import DirectorService
from project.services.genres_service import GenreService
from project.services.movies_service import MovieService
from project.services.users_service import UserService

genre_dao = GenreDAO()
movie_dao = MovieDAO()
director_dao = DirectorDAO()
user_dao = UserDAO()

genres_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)
director_service = DirectorService(dao=director_dao)
user_service = UserService(dao=user_dao)

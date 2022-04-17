from project.dao import GenreDAO
from project.dao.director import DirectorDAO
from project.dao.favorite import FavoriteDAO
from project.dao.movie import MovieDAO
from project.dao.user import UserDAO
from project.services.auth_service import AuthService
from project.services.directors_service import DirectorService
from project.services.favorite_service import FavoriteService
from project.services.genres_service import GenreService
from project.services.movies_service import MovieService
from project.services.users_service import UserService
from project.setup_db import db

genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)
director_dao = DirectorDAO(session=db.session)
user_dao = UserDAO(session=db.session)
favorite_dao = FavoriteDAO(session=db.session)

genre_service = GenreService(genre_dao)
movie_service = MovieService(movie_dao)
director_service = DirectorService(director_dao)
user_service = UserService(user_dao)
auth_service = AuthService(user_service)
favorite_service = FavoriteService(favorite_dao)

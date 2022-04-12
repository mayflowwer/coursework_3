from flask import request
from flask_restx import Namespace, Resource

from container import director_service

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        page = request.args.get('page')
        return director_service.get_all(page=page)


@directors_ns.route('/<int:user_id>')
class DirectorView(Resource):
    def get(self, director_id: int):
        return director_service.get_one(director_id)

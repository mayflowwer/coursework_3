from flask import request
from flask_restx import Namespace, Resource

from container import director_service
from project.schemas.director import DirectorSchema

directors_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        page = request.args.get('page')
        directors = director_service.get_all(page)
        return directors_schema.dump(directors)


@directors_ns.route('/<int:user_id>')
class DirectorView(Resource):
    def get(self, director_id: int):
        director = director_service.get_one(director_id)
        return director_schema.dump(director)

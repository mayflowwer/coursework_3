from marshmallow import Schema, fields


class FavoriteSchema(Schema):
    user_id = fields.Int()
    movie_id = fields.Int()

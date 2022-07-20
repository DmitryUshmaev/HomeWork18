# Модель для сущности жанров

from marshmallow import Schema, fields
from setup_db import db

"""Модель таблицы genre"""


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


"""Схема для работы с таблицей director"""


class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()

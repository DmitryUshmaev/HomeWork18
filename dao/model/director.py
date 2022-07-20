# Модель для сущности режиссеров

from marshmallow import Schema, fields
from setup_db import db

"""Модель таблицы director"""


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


"""Схема для работы с таблицей director"""


class DirectorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()

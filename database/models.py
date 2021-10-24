import datetime

from database.db import db


class Image(db.Document):
    id = db.SequenceField()
    src = db.StringField(required=True)


class Card(db.Document):
    name = db.StringField(required=True)
    type = db.StringField(required=True)
    details = db.DictField(required=True)


class Sound(db.Document):
    src = db.StringField(required=True)
    text = db.StringField(required=False)


class TestCard(db.Document):
    message = db.StringField(default="")
    selectable = db.BooleanField(default=True)
    sound = db.ReferenceField(Sound)
    card = db.ReferenceField(Card)


class Test(db.Document):
    name = db.StringField(required=True)
    cards = db.ListField(db.ReferenceField(TestCard))

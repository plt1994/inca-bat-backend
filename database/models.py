import datetime

from database.db import db


class Image(db.Document):
    identifier = db.SequenceField()
    src = db.StringField(required=True)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)


class Card(db.Document):
    name = db.StringField(required=True)
    card_type = db.StringField(required=True)
    details = db.DictField(required=True)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)


class Sound(db.Document):
    filename = db.StringField(required=True)
    text = db.StringField(required=False)
    creator = db.StringField(required=True)
    length = db.IntField(required=True)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)


class TestCard(db.Document):
    message = db.StringField(default="")
    selectable = db.BooleanField(default=True)
    sound = db.ReferenceField(Sound)
    card = db.ReferenceField(Card)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)


class Test(db.Document):
    name = db.StringField(required=True)
    cards = db.ListField(db.ReferenceField(TestCard))
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)

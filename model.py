__author__ = 'Nick'
from peewee import *
db = SqliteDatabase("beer.db", threadlocals=True)


class DBModel(Model):
    class Meta:
        database = db


class BrewerySize(DBModel):
    id = PrimaryKeyField()
    label = CharField(default="")
    description = CharField(default="")


class Brewery(DBModel):
    id = PrimaryKeyField()
    name = CharField(default="")
    location = CharField(default="")
    image = CharField(default="")
    size = ForeignKeyField(BrewerySize)
    description = CharField(default="")


class BeerStyle(DBModel):
    id = PrimaryKeyField()
    label = CharField(default="")
    description = CharField(default="")


class Beer(DBModel):
    id = PrimaryKeyField()
    brewer = ForeignKeyField(Brewery)
    alcohol = FloatField(default=0.0)
    style = ForeignKeyField(BeerStyle)
    image = CharField(default="")
    name = CharField(default="")
    description = CharField(default="")

    def __unicode__(self):
        return self.name

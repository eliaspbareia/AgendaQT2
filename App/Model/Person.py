from peewee import *
from Model.BaseModel import BaseModel


class Person(BaseModel):
    id = AutoField()
    nomeperson = CharField(max_length=80, unique=True)
    emailperson = CharField()
    dtanascimentoperson = DateField()
    telefoneperson = CharField(max_length=14)


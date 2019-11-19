from peewee import *

db = MySQLDatabase(host="localhost", user="root", passwd="Bot9e0l1i2a1s7", database='agenda')


class BaseModel(Model):


    class Meta:
        database = db

import peewee
import os

PATH  = os.path.dirname(os.path.realpath(__file__))

db = peewee.SqliteDatabase(os.join(PATH,'people.db'))

class Person(peewee.Model):
    name = peewee.CharField(max_length=100)
    social_number = peewee.CharField(max_length=8)
    address = peewee.CharField(max_length=100)
    location = peewee.CharField(max_length=10)
    type = peewee.CharField(max_length=1)
    class Meta:
        database = db # This model uses the "people.db" database.

class Consult(peewee.Model):
    paciente = peewee.ForeignKeyField(Person,related_name="pac")
    doctor = peewee.ForeignKeyField(Person,related_name="doc")
    sintomas = peewee.CharField(max_length=100)
    diagnostico = peewee.CharField(max_length=100)
    tratamiento = peewee.CharField(max_length=100)
    notas = peewee.CharField(max_length=100)
    class Meta:
        database = db # This model uses the "people.db" database.


class ConsultExt(peewee.Model):
    paciente = peewee.ForeignKeyField(Person)
    doctor = peewee.CharField(max_length=100)
    sintomas = peewee.CharField(max_length=100)
    diagnostico = peewee.CharField(max_length=100)
    tratamiento = peewee.CharField(max_length=100)
    notas = peewee.CharField(max_length=100)
    location = peewee.CharField(max_length=100)

    class Meta:
        database = db # This model uses the "people.db" database.

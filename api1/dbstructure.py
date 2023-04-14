from peewee import *

db = MySQLDatabase('lab2api1', user='root', password='', host='localhost', port=3306)

class Tipocontribuyente(Model):
    nombre = CharField()
    descripcion = CharField()
    
    class Meta:
        database = db

class Datosventa(Model):
    nitcliente = CharField()
    nombrecliente = CharField()
    fechahora = DateTimeField()
    total = DecimalField(max_digits=10, decimal_places=4)
    tipocontribuyente = ForeignKeyField(Tipocontribuyente)

    class Meta:
        database = db

class Logs(Model):
    informacion = CharField()

    class Meta:
        database = db
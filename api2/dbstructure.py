from peewee import *

db = MySQLDatabase('lab2api2', user='root', password='', host='localhost', port=3306)


class Contabilidad(Model):
    montoiva = DecimalField(max_digits=10, decimal_places=4)
    totalsiniva = DecimalField(max_digits=10, decimal_places=4)
    total = DecimalField(max_digits=10, decimal_places=4)
    numeroventa = IntegerField()
   
    class Meta:
        database = db

class Fidelidadcliente(Model):
    nitcliente = CharField()
    contadorventas = IntegerField()
    montobonos = DecimalField(max_digits=10, decimal_places=4)

    class Meta:
        database = db

class Logs(Model):
    informacion = CharField()

    class Meta:
        database = db
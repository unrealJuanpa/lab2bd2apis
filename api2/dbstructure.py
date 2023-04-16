from peewee import *

db = MySQLDatabase('lab2api2', user='root', password='', host='localhost', port=3306)


class Contabilidad(Model):
    montoiva = DecimalField(max_digits=10, decimal_places=4) # sale del total Datosventa
    totalsiniva = DecimalField(max_digits=10, decimal_places=4) # sale del total Datosventa
    total = DecimalField(max_digits=10, decimal_places=4) # sale del total Datosventa
    numeroventa = IntegerField() # sale del id Datosventa
    nombretipocontribuyente = CharField() # nombre tipocontribuyente sale de Tipocontribuyente
    fechahora = DateTimeField() # sale del Datosventa
   
    class Meta:
        database = db

class Fidelidadcliente(Model):
    nitcliente = CharField() # sale del nitcliente Datosventa
    nombrecliente = CharField() # nombrecliente Datosventa
    contadorventas = IntegerField() # aumenta cada vez que se registra una venta
    montobonos = DecimalField(max_digits=10, decimal_places=4) # aumenta de 500 en 500

    class Meta:
        database = db

class Logs(Model):
    informacion = CharField()

    class Meta:
        database = db

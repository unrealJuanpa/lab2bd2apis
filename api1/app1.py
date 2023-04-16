from flask import Flask, request, jsonify
from dbstructure import *
import datetime
import requests
import json


app = Flask(__name__)
uriapi2 = 'http://127.0.0.1:6000'
db.connect()

@app.route('/tipocontribuyente', methods=['GET', 'POST'])
@app.route('/tipocontribuyente/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def manage_tipocontribuyente(id=None):
    try:
        req_data = request.get_json()

        if request.method == 'GET':
            if id: return jsonify(list(Tipocontribuyente.select().where(Tipocontribuyente.id == id).dicts()))
            return jsonify(list(Tipocontribuyente.select().dicts()))
        elif request.method == 'POST':
            Tipocontribuyente.create(**req_data)
            Logs.create(informacion=f"Se ha creado el tipo contribuyente {req_data['nombre']} en el momento: {datetime.datetime.now()}")
            return jsonify({'message': 'Data added successfully'})
        elif request.method == 'PUT':
            Tipocontribuyente.update(**req_data).where(Tipocontribuyente.id==id).execute()
            Logs.create(informacion=f"Se ha modificado el tipo contribuyente con id = {id} en el momento: {datetime.datetime.now()}")
            return jsonify({'message': 'Data updated successfully'})
        elif request.method == 'DELETE':
            Tipocontribuyente.delete_by_id(id)
            Logs.create(informacion=f"Se ha eliminado el tipo contribuyente con el id = {id} en el momento: {datetime.datetime.now()}")
            return jsonify({'message': 'Data deleted successfully'})
    except Exception as e:
        return jsonify({'message': str(e)})


@app.route('/datosventa', methods=['GET', 'POST'])
@app.route('/datosventa/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def manage_datosventa(id=None):
    try:
        req_data = request.get_json()

        if request.method == 'GET':
            if id: return jsonify(list(Datosventa.select().where(Datosventa.id == id).dicts()))
            return jsonify(list(Datosventa.select().dicts()))
        elif request.method == 'POST':
            ff = datetime.datetime.now()
            Datosventa.create(**req_data, fechahora=ff)
            Logs.create(informacion=f"Se ha creado el registro de venta para el cliente {req_data['nombrecliente']} en el momento: {ff}")


            idv = list(Datosventa.select().dicts())[-1]['id']
            ntc = str(list(Tipocontribuyente.select().where(Tipocontribuyente.id == req_data['tipocontribuyente']).dicts())[0]['nombre'])

            headers = {'Content-type': 'application/json'}
            dt = {
                "idventa": idv,
                "nitcliente": req_data['nitcliente'],
                "nombrecliente": req_data['nombrecliente'],
                "fechahora": str(ff),
                "total": req_data['total'],
                "nombretipocontribuyente": ntc
            }
            response = requests.post(url=uriapi2+'/contabilidad', data=json.dumps(dt), headers=headers) # algo esta pasando en esta linea
            return jsonify({'message': response.json()['message']})
        elif request.method == 'PUT':
            Datosventa.update(**req_data).where(Datosventa.id == id).execute()
            Logs.create(informacion=f"Se ha modificado el registro de datos venta con id = {id} en el momento: {datetime.datetime.now()}")
            return jsonify({'message': 'Data updated successfully'})
        elif request.method == 'DELETE':
            Datosventa.delete_by_id(id)
            Logs.create(informacion=f"Se ha eliminado el registro de datos venta con el id = {id} en el momento: {datetime.datetime.now()}")
            return jsonify({'message': 'Data deleted successfully'})
    except Exception as e:
        return jsonify({'message': str(e)})

if __name__ == '__main__':
    app.run(port=5000)

from flask import Flask, request, jsonify
from dbstructure import *
import datetime

app = Flask(__name__)
db.connect()

@app.route('/tipocontribuyente', methods=['POST'])
def add_data_tipoc():
    try:
        req_data = request.get_json()
        Tipocontribuyente.create(**req_data)
        Logs.create(informacion=f"Se ha creado el tipo contribuyente {req_data['nombre']} en el momento: {datetime.datetime.now()}")
        return jsonify({'message': 'Data added successfully'})
    except Exception as e:
        return jsonify({'message': f'{e}'})

@app.route('/tipocontribuyente', methods=['GET'])
def get_all_data_tipoc():
    try:
        return jsonify(list(Tipocontribuyente.select().dicts()))
    except Exception as e:
        return jsonify({'message': f'{e}'})

@app.route('/tipocontribuyente/<int:id>', methods=['GET'])
def get_tipoc_by_id(id):
    try:
        return jsonify(list(Tipocontribuyente.select().where(Tipocontribuyente.id == id).dicts()))
    except Exception as e:
        return jsonify({'message': f'{e}'})

@app.route('/tipocontribuyente/<int:id>', methods=['PUT'])
def put_tipoc(id):
    req_data = request.get_json()
    
    try:
        Tipocontribuyente.update(**req_data).where(Tipocontribuyente.id==id).execute()
        Logs.create(informacion=f"Se ha modificado el tipo contribuyente con id = {id} en el momento: {datetime.datetime.now()}")
        return jsonify({'message': 'Data updated successfully'})
    except Exception as e:
        return jsonify({'message': f'{e}'})


@app.route('/tipocontribuyente/<int:id>', methods=['DELETE'])
def delete_data_tipoc(id):
    try:
        Tipocontribuyente.delete_by_id(id)
        Logs.create(informacion=f"Se ha eliminado el tipo contribuyente con el id = {id} en el momento: {datetime.datetime.now()}")
        return jsonify({'message': 'Data deleted successfully'})
    except Exception as e:
        return jsonify({'message': f'{e}'})


@app.route('/datosventa', methods=['GET'])
def getdv():
    try:
        return jsonify(list(Datosventa.select().dicts()))
    except Exception as e:
        return jsonify({'message': f'{e}'})

@app.route('/datosventa/<int:id>', methods=['GET'])
def getdvi(id):
    try:
        return jsonify(list(Datosventa.select().where(Datosventa.id == id).dicts()))
    except Exception as e:
        return jsonify({'message': f'{e}'})

@app.route('/datosventa', methods=['POST'])
def postdv():
    try:
        req_data = request.get_json()
        ff = datetime.datetime.now()
        Datosventa.create(**req_data)
        Logs.create(informacion=f"Se ha creado el registro de venta para el cliente {req_data['nombrecliente']} en el momento: {ff}")
        return jsonify({'message': 'Data added successfully'})
    except Exception as e:
        return jsonify({'message': f'{e}'})
    
@app.route('/datosventa/<int:id>', methods=['PUT'])
def putdv(id):
    try:
        req_data = request.get_json()
        Datosventa.update(**req_data).where(Datosventa.id == id).execute()
        Logs.create(informacion=f"Se ha modificado el registro de datos venta con id = {id} en el momento: {datetime.datetime.now()}")
        return jsonify({'message': 'Data updated successfully'})
    except Exception as e:
        return jsonify({'message': f'{e}'})

@app.route('/datosventa/<int:id>', methods=['DELETE'])
def deletedv(id):
    try:
        Datosventa.delete_by_id(id)
        Logs.create(informacion=f"Se ha eliminado el registro de datos venta con el id = {id} en el momento: {datetime.datetime.now()}")
        return jsonify({'message': 'Data deleted successfully'})
    except Exception as e:
        return jsonify({'message': f'{e}'})

if __name__ == '__main__':
    app.run(port=5000)

from flask import Flask, request, jsonify
from dbstructure import *
import datetime

app = Flask(__name__)
db.connect()

@app.route('/tipocontribuyente', methods=['POST'])
def add_data_tipoc():
    try:
        req_data = request.get_json()
        Tipocontribuyente.create(nombre=req_data['nombre'], descripcion=req_data['descripcion'])
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
        Tipocontribuyente.update(nombre=req_data['nombre'], descripcion=req_data['descripcion']).where(Tipocontribuyente.id==id).execute()
        Logs.create(informacion=f"Se ha modificado el tipo contribuyente con id = {id} en el momento: {datetime.datetime.now()}")
        return jsonify({'message': 'Data updated successfully'})
    except Exception as e:
        return jsonify({'message': f'{e}'})


@app.route('/tipocontribuyente/<int:id>', methods=['DELETE'])
def delete_data_tipoc(id):
    # Eliminamos los datos de nuestra lista
    try:
        Tipocontribuyente.delete_by_id(id)
        Logs.create(informacion=f"Se ha eliminado el tipo contribuyente con el id = {id} en el momento: {datetime.datetime.now()}")
        return jsonify({'message': 'Data deleted successfully'})
    except Exception as e:
        return jsonify({'message': f'{e}'})


if __name__ == '__main__':
    app.run(port=5000)

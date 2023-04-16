from flask import Flask, request, jsonify
from dbstructure import *
import datetime


app = Flask(__name__)
db.connect()

@app.route('/contabilidad', methods=['GET', 'POST'])
@app.route('/contabilidad/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def manage_contabilidad(id=None):
    try:
        req_data = request.get_json()

        if request.method == 'GET':
            if id: return jsonify(list(Contabilidad.select().where(Contabilidad.id == id).dicts()))
            return jsonify(list(Contabilidad.select().dicts()))
        elif request.method == 'POST':
            iva = float(req_data['total'])*0.12
            Contabilidad.create(montoiva=iva, totalsiniva=float(req_data['total'])-iva, total=req_data['total'], numeroventa=req_data['idventa'], nombretipocontribuyente=req_data['nombretipocontribuyente'], fechahora=req_data['fechahora'])
            
            rbusq = list(Fidelidadcliente.select().where(Fidelidadcliente.nitcliente == req_data['nitcliente']).dicts())
            if len(rbusq) == 0:
                Fidelidadcliente.create(nitcliente=req_data['nitcliente'], nombrecliente=req_data['nombrecliente'], contadorventas=1, montobonos=0)
            else:
                cventas = int(rbusq[0]['contadorventas']) + 1
                montobonos = float(rbusq[0]['montobonos'])
                if cventas % 3 == 0: montobonos += 500
                Fidelidadcliente.update(contadorventas = cventas, montobonos = montobonos).where(Fidelidadcliente.nitcliente == req_data['nitcliente']).execute()

            Logs.create(informacion=f"Se ha creado el registro de contabilidad y se ha actualizado fidelidad del cliente con el nit: {req_data['nitcliente']} en el momento: {datetime.datetime.now()}")
            return jsonify({'message': 'Todo correcto'})
        elif request.method == 'PUT':
            Contabilidad.update(**req_data).where(Contabilidad.id == id).execute()
            Logs.create(informacion=f"Se ha modificado el registro de contabilidad con el id = {id} en el momento: {datetime.datetime.now()}")
            return jsonify({'message': 'Data updated successfully'})
        elif request.method == 'DELETE':
            Contabilidad.delete_by_id(id)
            Logs.create(informacion=f"Se ha eliminado el registro de contabilidad con el id = {id} en el momento: {datetime.datetime.now()}")
            return jsonify({'message': 'Data deleted successfully'})
    except Exception as e:
        return jsonify({'message': str(e)})
    

@app.route('/fidelidadcliente', methods=['GET'])
@app.route('/fidelidadcliente/<int:id>', methods=['GET'])
def manage_fidelidadcliente(id=None):
    if id: return jsonify(list(Fidelidadcliente.select().where(Fidelidadcliente.id == id).dicts()))
    return jsonify(list(Fidelidadcliente.select().dicts()))


if __name__ == '__main__':
    app.run(port=6000)
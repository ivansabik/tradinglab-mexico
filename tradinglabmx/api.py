from flask import Flask, jsonify, request
from modelos import Emisora

app = Flask(__name__)

# Endpoints API REST
@app.route('/')
def index():
	return 'La racine'

@app.route('/api/emisoras')
def api_emisoras():
    emisora = Emisora()
    emisoras = emisora.todas_json()
    return jsonify(lista_emisoras = emisoras)
    
@app.route('/api/emisora')
def api_emisora():
    if 'clave' in request.args:
        clave = request.args['clave']
        emisora = Emisora()
        return jsonify(emisora.buscar(clave))
    else:
        error = {'error': 'Falta el parametro "clave" con el ticker de la emisora'}
        return jsonify(error)

if __name__== '__main__':
    app.run(debug=True)

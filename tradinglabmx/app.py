from flask import Flask, url_for, jsonify, render_template, request
from modelos import Emisora

app = Flask(__name__)

# Endpoints html
@app.route('/')
def emisoras():
    emisora = Emisora()
    emisoras = emisora.todas_json()
    print emisoras
    return render_template('emisoras.html', emisoras = emisoras)
    
@app.route('/emisora')
def emisora():
    return render_template('emisora.html')
    
@app.route('/estrategia')
def estrategia():
    return render_template('estrategia.html')
    
# API
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

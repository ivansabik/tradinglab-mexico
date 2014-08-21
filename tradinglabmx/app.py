from flask import Flask, url_for, jsonify, render_template
from modelos import Emisora

app = Flask(__name__)

# Endpoints html
@app.route('/')
def emisoras():
	return render_template('emisoras.html')
	
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
	emisoras = emisora.todas()
	return jsonify(lista_emisoras = emisoras)
	
@app.route('/api/emisora')
def api_emisora():
	emisora = Emisora()
	emisora.clave_bmv = 'WALMEX'
	emisora.nombre = 'Wal Mart'
	return jsonify(emisora.__dict__)
	
if __name__== '__main__':
    app.run(debug=True)

from flask import Flask, url_for, render_template, request, redirect
from modelos import Emisora

app = Flask(__name__)

# Endpoints html
@app.route('/')
def index():
	return redirect(url_for('emisoras'))
	
@app.route('/emisoras')
def emisoras():
    emisora = Emisora()
    emisoras = emisora.todas_json()
    return render_template('emisoras.html', emisoras = emisoras)
    
@app.route('/emisora')
def emisora():
    if 'clave' in request.args:
        clave = request.args['clave']
        emisora = Emisora()
        return render_template('emisora.html', emisora = emisora.buscar(clave))
    else:
        return render_template('emisoras.html')
    
@app.route('/estrategia')
def estrategia():
    return render_template('estrategia.html')

if __name__== '__main__':
    app.run(debug=True)

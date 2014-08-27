from flask import Flask, url_for, render_template, request, redirect
from json import dumps
from modelos import Emisora
import collections
import time

app = Flask(__name__)

# Endpoints html
@app.route('/')
def index():
	return redirect(url_for('emisoras'))
	
@app.route('/emisoras')
def emisoras():
    emisora = Emisora()
    if 'sector' in request.args:
        id_sector = request.args['sector']
        emisoras = emisora.sector(id_sector)
    else:
        emisoras = emisora.todas()
    return render_template('emisoras.html', emisoras=emisoras)
    
@app.template_filter('fecha_cotizacion')
def _filter_fecha_cotizacion(fecha_epoch):
    fecha_epoch = int(fecha_epoch)
    fecha = time.gmtime(fecha_epoch/1000)
    return time.strftime('%m-%d-%Y', fecha)
    
@app.route('/emisora')
def emisora():
    if 'clave' in request.args:
        clave = request.args['clave']
        emisora = Emisora()
        emisora = emisora.buscar(clave)
        if not emisora.get('error'):
            precios = emisora['info_historica']['adj_close']
            # Convierte keys a ints (numeros)
            # Hay que ordenar fechas para http://www.highcharts.com/errors/15
            precios = {int(k):int(v) for k,v in precios.items()}
            precios = collections.OrderedDict(sorted(precios.items()))
            precios = precios.items()
            return render_template('emisora.html', emisora=emisora, precios=dumps(precios))
        else:
            # TODO: tmpl con mensaje que no encontro clave
            return redirect(url_for('emisoras'))
    else:
        return render_template('emisoras.html')
    
@app.route('/estrategia')
def estrategia():
    return render_template('estrategia.html')

if __name__== '__main__':
    app.run(debug=True)

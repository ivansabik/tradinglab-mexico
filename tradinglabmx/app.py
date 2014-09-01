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
   
@app.route('/comparar')
def comparar():
	emisora = Emisora()
	if not 'emisora' in request.args:
		emisoras = emisora.todas()
		return render_template('comparar-seleccion.html', emisoras=emisoras)
	else:
		clave_emisora_1 = request.args['emisora']
		clave_emisora_2 = request.args['emisora2']
		emisora_1 = emisora.buscar(clave_emisora_1)
		emisora_2 = emisora.buscar(clave_emisora_2)
		rend_emisora_1 = emisora_1['info_historica']['rendimientos']
		rend_emisora_2 = emisora_2['info_historica']['rendimientos']
		media_emisora_1 = emisora_1['media_rendimientos']
		std_emisora_1 = emisora_1['std_rendimientos']
		media_emisora_2 = emisora_2['media_rendimientos']
		std_emisora_2 = emisora_2['std_rendimientos']
		rend_emisora_1 = {int(k):int(v) for k,v in rend_emisora_1.items()}
		rend_emisora_1 = collections.OrderedDict(sorted(rend_emisora_1.items()))
		
		
        rend_emisora_1 = rend_emisora_1.items()
		
        datos = {'rend_emisora_1': rend_emisora_1, 'rend_emisora_2': rend_emisora_2, 'media_emisora_1': media_emisora_1, 'media_emisora_2': media_emisora_2, 'std_emisora_1': std_emisora_1, 'std_emisora_2':std_emisora_2}
        return render_template('comparar-resultados.html', emisora_1=emisora_1, emisora_2=emisora_2, datos=dumps(datos))

if __name__== '__main__':
    app.run(debug=True)

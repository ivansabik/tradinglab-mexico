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
    
@app.template_filter('indicador')
def _filter_indicador(valor):
    return '{0:.4f}'.format(valor)
    
@app.template_filter('porcentaje')
def _filter_porcentaje(valor):
    return '{0:.4f}'.format(valor*100) + ' %'
    
@app.route('/emisora')
def emisora():
    if 'clave' in request.args:
        clave = request.args['clave']
        emisora = Emisora()
        emisora = emisora.buscar(clave)
        if not emisora.get('error'):
            # TODO: conversion en funcion, se usa 8 veces
            # Convierte keys a ints (numeros), ordenados para highcharts
            cierre_aj = emisora['info_historica']['adj_close']
            cierre_aj = {int(k):float(v) for k,v in cierre_aj.items()}
            cierre_aj = collections.OrderedDict(sorted(cierre_aj.items()))
            cierre_aj = cierre_aj.items()
            volumen = emisora['info_historica']['volume']
            volumen = {int(k):float(v) for k,v in volumen.items()}
            volumen = collections.OrderedDict(sorted(volumen.items()))
            volumen = volumen.items()
            mavg5 = emisora['info_historica']['mavg5']
            mavg5 = {int(k):float(v) for k,v in mavg5.items()}
            mavg5 = collections.OrderedDict(sorted(mavg5.items()))
            mavg5 = mavg5.items()
            mavg10 = emisora['info_historica']['mavg10']
            mavg10 = {int(k):float(v) for k,v in mavg10.items()}
            mavg10 = collections.OrderedDict(sorted(mavg10.items()))
            mavg10 = mavg10.items()
            mavg20 = emisora['info_historica']['mavg20']
            mavg20 = {int(k):float(v) for k,v in mavg20.items()}
            mavg20 = collections.OrderedDict(sorted(mavg20.items()))
            mavg20 = mavg20.items()
            mavg50 = emisora['info_historica']['mavg50']
            mavg50 = {int(k):float(v) for k,v in mavg50.items()}
            mavg50 = collections.OrderedDict(sorted(mavg50.items()))
            mavg50 = mavg50.items()
            mavg200 = emisora['info_historica']['mavg50']
            mavg200 = {int(k):float(v) for k,v in mavg200.items()}
            mavg200 = collections.OrderedDict(sorted(mavg200.items()))
            mavg200 = mavg200.items()
            data = {'cierre_aj': cierre_aj, 'volumen': volumen, 'mavg5': mavg5, 'mavg10': mavg10, 'mavg20': mavg20, 'mavg50': mavg50, 'mavg200': mavg200}
            return render_template('emisora.html', emisora=emisora, data=dumps(data))
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
		rend_emisora_1 = {int(k):float(v) for k,v in rend_emisora_1.items() if v is not None}
		rend_emisora_1 = collections.OrderedDict(sorted(rend_emisora_1.items()))
		rend_emisora_1 = rend_emisora_1.items()	
		rend_emisora_2 = emisora_2['info_historica']['rendimientos']
		rend_emisora_2 = {int(k):float(v) for k,v in rend_emisora_2.items() if v is not None}
		rend_emisora_2 = collections.OrderedDict(sorted(rend_emisora_2.items()))
		rend_emisora_2 = rend_emisora_2.items()	
		media_emisora_1 = emisora_1['estadisticas']['rendimientos_media']
		std_emisora_1 = emisora_1['estadisticas']['rendimientos_std']
		media_emisora_2 = emisora_2['estadisticas']['rendimientos_media']
		std_emisora_2 = emisora_2['estadisticas']['rendimientos_std']
        data = {'rend_emisora_1': rend_emisora_1, 'rend_emisora_2': rend_emisora_2, 'media_emisora_1': media_emisora_1, 'media_emisora_2': media_emisora_2, 'std_emisora_1': std_emisora_1, 'std_emisora_2':std_emisora_2}
        return render_template('comparar-resultados.html', emisora_1=emisora_1, emisora_2=emisora_2, data=dumps(data))

if __name__== '__main__':
    app.run(debug=True)

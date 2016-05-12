from flask import Flask, url_for, render_template, request, redirect
from json import dumps
from modelos import Emisora
import collections
import time
import pandas as pd
from modelos import MovimientoTrading
from modelos import CompraVenta
from datetime import datetime

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
    return '{0:.6f}'.format(valor)


@app.template_filter('porcentaje')
def _filter_porcentaje(valor):
    return '{0:.6f}'.format(valor * 100) + ' %'


@app.template_filter('entero')
def _filter_entero(valor):
    return '{0:,.0f}'.format(valor)


@app.route('/emisora')
def emisora():
    if 'clave' in request.args:
        clave = request.args['clave']
        emisora = Emisora()
        emisora = emisora.buscar(clave)
        if not emisora.get('error'):
            # TODO: conversion en funcion, se usa 8 veces
            # Convierte keys a ints (numeros), ordenados para highcharts
            cierre_aj = _ordena_keys(emisora['info_historica']['adj_close'])
            volumen = _ordena_keys(emisora['info_historica']['volume'])
            mavg5 = _ordena_keys(emisora['info_historica']['mavg5'])
            mavg10 = _ordena_keys(emisora['info_historica']['mavg10'])
            mavg20 = _ordena_keys(emisora['info_historica']['mavg20'])
            mavg50 = _ordena_keys(emisora['info_historica']['mavg50'])
            mavg200 = _ordena_keys(emisora['info_historica']['mavg50'])
            data = {'cierre_aj': cierre_aj, 'volumen': volumen, 'mavg5': mavg5, 'mavg10': mavg10,
                    'mavg20': mavg20, 'mavg50': mavg50, 'mavg200': mavg200}
            return render_template('emisora.html', emisora=emisora, data=dumps(data))
        else:
            # TODO: tmpl con mensaje que no encontro clave
            return redirect(url_for('emisoras'))
    else:
        return render_template('emisoras.html')


@app.route('/comparar')
def comparar():
    emisora = Emisora()
    if not ('emisora' and 'emisora') in request.args:
        emisoras = emisora.todas()
        return render_template('comparar-seleccion.html', emisoras=emisoras)
    else:
        clave_emisora_1 = request.args['emisora']
        clave_emisora_2 = request.args['emisora2']
        emisora_1 = emisora.buscar(clave_emisora_1)
        emisora_2 = emisora.buscar(clave_emisora_2)
        rend_emisora_1 = _ordena_keys(emisora_1['info_historica']['rendimientos'])
        rend_emisora_2 = _ordena_keys(emisora_2['info_historica']['rendimientos'])
        media_emisora_1 = emisora_1['estadisticas']['rendimientos_media']
        std_emisora_1 = emisora_1['estadisticas']['rendimientos_std']
        media_emisora_2 = emisora_2['estadisticas']['rendimientos_media']
        std_emisora_2 = emisora_2['estadisticas']['rendimientos_std']
        precios_emisora_1 = _ordena_keys(emisora_1['info_historica']['adj_close'])
        precios_emisora_2 = _ordena_keys(emisora_2['info_historica']['adj_close'])
        serie_precios_1 = pd.Series(emisora_1['info_historica']['adj_close'])
        serie_precios_2 = pd.Series(emisora_2['info_historica']['adj_close'])
        corr_precio = serie_precios_1.corr(serie_precios_2)
        serie_rendimientos_1 = pd.Series(emisora_1['info_historica']['rendimientos'])
        serie_rendimientos_2 = pd.Series(emisora_2['info_historica']['rendimientos'])
        corr_rendimiento = serie_rendimientos_1.corr(serie_rendimientos_2)
        data = {'precios_emisora_1': precios_emisora_1, 'precios_emisora_2': precios_emisora_2,
                'rend_emisora_1': rend_emisora_1, 'rend_emisora_2': rend_emisora_2,
                'media_emisora_1': media_emisora_1, 'media_emisora_2': media_emisora_2,
                'std_emisora_1': std_emisora_1, 'std_emisora_2': std_emisora_2}
        return render_template('comparar-resultados.html', emisora_1=emisora_1, emisora_2=emisora_2,
                               corr_precio=corr_precio, corr_rendimiento=corr_rendimiento,
                               data=dumps(data))


@app.route('/estrategia', methods=['GET', 'POST'])
def estrategia():
    if request.method != 'POST':
        emisora = Emisora()
        emisoras = emisora.todas()
        return render_template('estrategia-seleccion.html', emisoras=emisoras)
    else:
        movimientos = []
        for movimiento in range(1, 11):
            clave_emisora = request.form.get('emisora' + str(movimiento), None)
            fecha = request.form.get('fecha' + str(movimiento), None)
            num_acciones = float(request.form.get('numacc' + str(movimiento), None))
            if clave_emisora:
                emisora = Emisora()
                emisora.buscar(clave_emisora, info_hist=False, formato_json=False)
                movimiento = MovimientoTrading()
                movimiento.num_acciones = num_acciones
                movimiento.emisora = emisora.clave_yahoo
                movimiento.fecha = datetime.strptime(fecha, '%d/%m/%y')
                movimientos.append(movimiento)
        trading = CompraVenta(movimientos)
        perf = trading.run()
        perf['returns_cum'] = perf['returns'].cumsum()
        perf['pnl_cum'] = perf['pnl'].cumsum()
        return render_template('estrategia-resultados.html', perf=perf.to_dict())


def _ordena_keys(columna):
    columna = {int(k): float(v) for k, v in columna.items()}
    columna = collections.OrderedDict(sorted(columna.items()))
    columna = columna.items()
    return columna

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)

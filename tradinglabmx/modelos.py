import json
import datetime
import pandas as pd
import pandas.io.data

# Emisora
class Emisora:
    def buscar(self, clave, fecha_inicio = '', fecha_fin = ''):
        json_data = open('emisoras.json')
        emisoras_json = json.load(json_data)
        for emisora_json in emisoras_json:
            clave_json  = emisora_json.get('clave', '')
            clave_yahoo  = emisora_json.get('clave_yahoo', '')
            if clave == clave_json:
                # Busca info de yahoo
                if(clave_yahoo != ''):
                    datos = pd.io.data.get_data_yahoo(clave_yahoo, 
                                    start = datetime.datetime(1990, 1, 1), 
                                    # TODO: Fecha actual
                                    end = datetime.datetime(2015, 1, 1))
                    datos_json = json.loads(datos.to_json(date_format = 'iso'))
                    emisora_json['info_historica'] = datos_json
                return emisora_json
        return {'resultado': 'No existe ninguna emisora con esa clave'}
        
    def todas_json(self):
        json_data = open('emisoras.json')
        emisoras_json = json.load(json_data)
        return emisoras_json

# Movimiento de trading
class MovimientoTrading:
    is_compra = ''
    num_acciones = ''
    emisora = ''
    fecha = ''

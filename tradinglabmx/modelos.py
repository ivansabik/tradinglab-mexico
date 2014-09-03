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
            if clave.upper() == clave_json:
                # Busca info de yahoo
                if(clave_yahoo != ''):
                    datos = pd.io.data.get_data_yahoo(clave_yahoo, start = datetime.datetime(1990, 1, 1))
                    datos.rename(columns={'Open': 'open'}, inplace=True)
                    datos.rename(columns={'High': 'high'}, inplace=True)
                    datos.rename(columns={'Low': 'low'}, inplace=True)
                    datos.rename(columns={'Close': 'close'}, inplace=True)
                    datos.rename(columns={'Volume': 'volume'}, inplace=True)
                    datos.rename(columns={'Adj Close': 'adj_close'}, inplace=True)
                    datos['rendimientos'] = datos['adj_close'].pct_change()
                    datos['mavg5'] = pd.ewma(datos['adj_close'], 5)
                    datos['mavg10'] = pd.ewma(datos['adj_close'], 10)
                    datos['mavg20'] = pd.ewma(datos['adj_close'], 20)
                    datos['mavg50'] = pd.ewma(datos['adj_close'], 50)
                    datos['mavg200'] = pd.ewma(datos['adj_close'], 200)
                    datos_json = json.loads(datos.to_json())
                    emisora_json['info_historica'] = datos_json
                    emisora_json['estadisticas'] = {}
                    emisora_json['estadisticas']['rendimientos_media'] = datos['rendimientos'].mean()
                    emisora_json['estadisticas']['rendimientos_std'] = datos['rendimientos'].std()
                    emisora_json['estadisticas']['precio_alto'] = datos['close'].max()
                    emisora_json['estadisticas']['precio_bajo'] = datos['close'].min()
                    emisora_json['estadisticas']['precio_media'] = datos['close'].mean()
                    emisora_json['estadisticas']['precio_std'] = datos['close'].std()
                else:
                    emisora_json['info_historica'] = {'open': {}, 'high': {}, 'low': {}, 'close': {}, 'volume': {}, 'adj_close': {}}
                return emisora_json
        return {'error': 'No existe ninguna emisora con esa clave'}
        
    def todas(self):
        json_data = open('emisoras.json')
        emisoras_json = json.load(json_data)
        return emisoras_json
        
    def sector(self, id_sector):
        json_data = open('emisoras.json')
        emisoras_json = json.load(json_data)
        emisoras_sector = []
        for emisora_json in emisoras_json:
            id_sector_json  = emisora_json.get('id_sector', '')
            if int(id_sector) == id_sector_json:
                emisoras_sector.append(emisora_json)
        return emisoras_sector

# Movimiento de trading
class MovimientoTrading:
    is_compra = ''
    num_acciones = ''
    emisora = ''
    fecha = ''
    
# Portafolio
class Portafolio:
    acciones = [{'emisora': 'ALPEK', 'peso': 0.25}]
    

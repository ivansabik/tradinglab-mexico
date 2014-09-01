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
                    media_rendimientos = datos['rendimientos'].mean()
                    std_rendimientos = datos['rendimientos'].std()
                    datos_json = json.loads(datos.to_json())
                    emisora_json['info_historica'] = datos_json
                    emisora_json['media_rendimientos'] = media_rendimientos
                    emisora_json['std_rendimientos'] = std_rendimientos
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
    

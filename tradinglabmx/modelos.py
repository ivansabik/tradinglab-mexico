import json

# Emisora
class Emisora:


	def get_emisoras(self):
		json_data = open('emisoras.json')
		emisoras_json = json.load(json_data)
		emisoras = []
		for emisora_json in emisoras_json:
			emisora = Emisora()
			clave  = emisora_json['clave']
			nombre = emisora_json['nombre']
			clave_yahoo = emisora_json['clave_yahoo']
			clave_bloomberg = emisora_json['clave_bloomberg']
			#fecha_constitucion = emisora_json['fecha_constitucion']
			#fecha_listado = emisora_json['fecha_listado']
			#sector = emisora_json['sector']
			#subsector = emisora_json['subsector']
			#ramo = emisora_json['ramo']
			#subramo = emisora_json['subramo']
			emisoras.append(emisora)
		return emisoras

# Movimiento de trading
class MovimientoTrading:
	is_compra = ''
	num_acciones = ''
	emisora = ''
	fecha = ''



import json

# Emisora
class Emisora:


	def get_emisoras(self):
		json_data = open('emisoras.json')
		emisoras_json = json.load(json_data)
		emisoras = []
		for emisora_json in emisoras_json:
			emisora = Emisora()
			clave  = emisora_json.get('clave', '')
			nombre = emisora_json.get('nombre', '')
			clave_yahoo = emisora_json.get('clave_yahoo', '')
			clave_bloomberg = emisora_json.get('clave_bloomberg', '')
			fecha_constitucion = emisora_json.get('fecha_constitucion', '')
			fecha_listado = emisora_json.get('fecha_listado', '')
			sector = emisora_json.get('sector', '')
			subsector = emisora_json.get('subsector', '')
			ramo = emisora_json.get('ramo', '')
			subramo = emisora_json.get('subramo', '')
			emisoras.append(emisora)
		return emisoras

# Movimiento de trading
class MovimientoTrading:
	is_compra = ''
	num_acciones = ''
	emisora = ''
	fecha = ''



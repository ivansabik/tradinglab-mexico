import json

# Emisora
class Emisora:
	
	def busca(self, clave = 'BMV'):
		# hier kommt was
		return ''

	# La clase esta pensada para la API, por default regresa como dict
	# TODO: renombrar a todas_json y devolver directo el JSON leido
	def todas(self, as_dict = True):
		json_data = open('emisoras.json')
		emisoras_json = json.load(json_data)
		emisoras = []
		for emisora_json in emisoras_json:
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
			if as_dict:
				emisora = {
					'clave': clave,
					'nombre': nombre,
					'clave_yahoo': clave_yahoo,
					'clave_bloomberg': clave_bloomberg,
					'fecha_constitucion': fecha_constitucion,
					'fecha_listado': fecha_listado,
					'sector': sector,
					'subsector': subsector,
					'ramo': ramo,
					'subramo': subramo
				}
			else:
				emisora = Emisora()
				# Aqui va algo si se quiere como objeto (no dict)
			emisoras.append(emisora)
		return emisoras
		
	def info_historica(self, fecha_inicio = '', fecha_fin = ''):
		# hier kommt was
		return ''

# Movimiento de trading
class MovimientoTrading:
	is_compra = ''
	num_acciones = ''
	emisora = ''
	fecha = ''

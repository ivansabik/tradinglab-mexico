from modelos import Emisora

emisora = Emisora()
emisora.clave_bmv = 'WALMEX'
emisora.nombre = 'Wal Mart'

print emisora.clave_bmv
print emisora.nombre

from modelos import MovimientoTrading

movimiento = MovimientoTrading()
movimiento.is_compra = True
movimiento.num_acciones = 500

print movimiento.is_compra
print movimiento.num_acciones

print emisora.get_emisoras()
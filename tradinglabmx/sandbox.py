from modelos import MovimientoTrading

movimiento = MovimientoTrading()
movimiento.is_compra = True
movimiento.num_acciones = 500

print movimiento.is_compra
print movimiento.num_acciones

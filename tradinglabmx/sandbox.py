from modelos import MovimientoTrading
from modelos import CompraVenta
import matplotlib.pyplot as plt
import matplotlib as mpl
import zipline as zp
from datetime import datetime

movimientos = []

movimiento = MovimientoTrading()
movimiento.num_acciones = 500
movimiento.emisora = 'ALSEA.MX'
movimiento.fecha = datetime(2010, 3, 1)
movimientos.append(movimiento)

movimiento = MovimientoTrading()
movimiento.num_acciones = -500
movimiento.emisora = 'ALSEA.MX'
movimiento.fecha = datetime(2013, 3, 1)
movimientos.append(movimiento)

movimiento = MovimientoTrading()
movimiento.num_acciones = 500
movimiento.emisora = 'KOFL.MX'
movimiento.fecha = datetime(2011, 2, 5)
movimientos.append(movimiento)

movimiento = MovimientoTrading()
movimiento.num_acciones = 500
movimiento.emisora = 'GFNORTEO.MX'
movimiento.fecha = datetime(2011, 8, 8)
movimientos.append(movimiento)

movimiento = MovimientoTrading()
movimiento.num_acciones = -50
movimiento.emisora = 'GFNORTEO.MX'
movimiento.fecha = datetime(2012, 8, 8)
movimientos.append(movimiento)

trading = CompraVenta(movimientos)
data = trading.data
perf = trading.run(data)

print perf['capital_used'].head()
print perf['starting_cash'].head()
print perf['ending_cash'].head()
print perf['returns'].head()

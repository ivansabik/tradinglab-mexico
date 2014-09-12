from modelos import MovimientoTrading

movimiento = MovimientoTrading()
movimiento.is_compra = True
movimiento.num_acciones = 500

print movimiento.is_compra
print movimiento.num_acciones


import pandas as pd
import pandas.io.data
import numpy as np
import pytz
from datetime import datetime
import zipline as zp
import matplotlib.pyplot as plt
import matplotlib as mpl

# Info de compra
num_acciones = 1
dia_compra, mes_compra, anio_compra = 1, 3, 2010
dia_venta, mes_venta, anio_venta = 1, 3, 2013

# Datos para Elektra (datetime en formato AAAA/MM/DD)
start = datetime(anio_compra, mes_compra, dia_compra, 0, 0, 0, 0, pytz.utc)
end = datetime(anio_venta, mes_venta, dia_venta + 5, 0, 0, 0, 0, pytz.utc)
data = zp.utils.factory.load_from_yahoo(stocks=['ELEKTRA.MX'], indexes={}, start=start,
                                        end=end, adjusted=False)
                                        
class BuyLektra(zp.TradingAlgorithm):
    def handle_data(self, data):
        fecha = data['ELEKTRA.MX'].dt
        precio = data['ELEKTRA.MX'].price
        # Buy primo, buy
        if(fecha.day == dia_compra and fecha.month == mes_compra and fecha.year == anio_compra):
            self.order('ELEKTRA.MX', num_acciones)
        # Sell primo, sell
        elif(fecha.day == dia_venta and fecha.month == mes_venta and fecha.year == anio_venta):
            self.order('ELEKTRA.MX', -num_acciones)

algo = BuyLektra()
perf = algo.run(data)

perf['portfolio_value'].plot()
print perf['portfolio_value']

# Estrategia de compra al inicio, vende al final
dia_compra, mes_compra, anio_compra = 1, 3, 2010
dia_venta, mes_venta, anio_venta = 1, 3, 2013

# dependencias
import pandas as pd
import pandas.io.data
import numpy as np
import pytz
from datetime import datetime
import zipline as zp
import matplotlib.pyplot as plt
import matplotlib as mpl

# datos (datetime en formato AAAA/MM/DD)
start = datetime(anio_compra, mes_compra, dia_compra, 0, 0, 0, 0, pytz.utc)
end = datetime(anio_venta, mes_venta, dia_venta + 5, 0, 0, 0, 0, pytz.utc)
data = zp.utils.factory.load_from_yahoo(stocks=['ELEKTRA.MX'], indexes={}, start=start,
                                        end=end, adjusted=False)

# estrategia
class BuyLektra(zp.TradingAlgorithm):
    def handle_data(self, data):
        fecha = data['ELEKTRA.MX'].dt
        precio = data['ELEKTRA.MX'].price
        # print 'fecha: ' + str(fecha.day) + ' / ' + str(fecha.month) + ' / ' + str(fecha.year)
        # print 'precio: ' + str(precio)
        if(fecha.day == dia_compra and fecha.month == mes_compra and fecha.year == anio_compra):
            print 'buy primo, buy'
            self.order('ELEKTRA.MX', 1)
        elif(fecha.day == dia_venta and fecha.month == mes_venta and fecha.year == anio_venta):
            print 'sell primo, sell'
            self.order('ELEKTRA.MX', -1)
# trade
algo = BuyLektra()
perf = algo.run(data)
print perf['portfolio_value']

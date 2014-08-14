# dependencias
import pandas as pd
import pandas.io.data
import numpy as np
import pytz
from datetime import datetime
import zipline as zp
from zipline.finance.slippage import FixedSlippage
import matplotlib.pyplot as plt
import matplotlib as mpl

# plot
mpl.rc('figure', figsize=(8, 7))

start = datetime(2000, 1, 1, 0, 0, 0, 0, pytz.utc)
end = datetime(2015, 1, 1, 0, 0, 0, 0, pytz.utc)
data = zp.utils.factory.load_from_yahoo(stocks=['ELEKTRA.MX'], indexes={}, start=start,
                                        end=end, adjusted=False)
data.plot()
plt.show()

# estrategia
class BuyApple(zp.TradingAlgorithm): # inherit from TradingAlgorithm
    def handle_data(self, data): # overload handle_data() method
        self.order('ELEKTRA.MX', 1) # stock (='AAPL') to order and amount (=1 shares)

# trade
algo = BuyApple()
perf = algo.run(data)
perf.to_csv('elektraperf.csv')

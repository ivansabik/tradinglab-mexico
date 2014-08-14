import pandas as pd
import pandas.io.data
import numpy as np

import pytz
from datetime import datetime

import zipline as zp

from zipline.finance.slippage import FixedSlippage

import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rc('figure', figsize=(8, 7))

start = datetime(1990, 1, 1, 0, 0, 0, 0, pytz.utc)
end = datetime(2002, 1, 1, 0, 0, 0, 0, pytz.utc)
data = zp.utils.factory.load_from_yahoo(stocks=['ELEKTRA.MX'], indexes={}, start=start,
                                        end=end, adjusted=False)
data.plot()
plt.show()

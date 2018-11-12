import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# plt.plot(np.arange(10))

# series - ordered dictionary
# data frames - 2D data structure (like a table)

stocks = pd.Series([12,10,-8,-6,4],index=["fennel","corriander","tamarind","pepper","cumin"])
print(stocks)
print(stocks.index)
print(stocks['corriander'])

if stocks['tamarind'] > 5:
    print("Safe")
else:
    print("Alert!!")

stocks['indianjeera'] = 23
print(stocks)


print("Filtering stocks greater than 5\n",stocks[stocks>5]) # filter the values as per condition
print(stocks.values) # displays the values
print(2*stocks[stocks>0]) # filter and changes value as well

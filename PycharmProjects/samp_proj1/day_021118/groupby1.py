
import pandas as pd, numpy as np

#stocks = pd.Series([12,10,-8,-6,4],index=["fennel","corriander","tamarind","pepper","cumin"])

stocks = pd.DataFrame({'spice':['tamarind','corriander','corriander','cumin','cumin','corriander','corriander','cumin'],
                       'brand':['everest','mdh','mdh','patanjali','mdh','everest','mdh','patanjali'],
                       'price':[23,14,21,18,13,15,15,12],
                       'qty':[4,6,0,-5,13,23,9,5]})

# grouped_stocks = stocks['spice'].groupby(stocks['spice'])
# print(grouped_stocks.mean)

print(stocks['price'].groupby([stocks['brand'],stocks['spice']]).mean())

print(stocks.groupby('price').mean())
print(stocks.groupby('price').size())
print(stocks.groupby('spice').groups)

for name,group in stocks.groupby('spice'):
    print("This is name",name)
    print("This is group",group)

pieces = dict(list(stocks.groupby('spice')))
print("Pieces of tamarind\n",pieces['tamarind'])
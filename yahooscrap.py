'''
PROBLEMA: con pandas.DataFrame() stampa le prime 5 rows
e poi salta dirtettamente alla 245

                   Names     Prices    Changes %Changes MarketCap    Volume   Supplys
0            Bitcoin USD  26,926.12    -905.30   -3.25%  520.476B    16.31B    19.33M
1           Ethereum USD   1,709.44     -58.42   -3.30%  209.191B    7.357B  122.374M
2             Tether USD     1.0000    -0.0007   -0.07%   79.181B   25.778B    79.18B
3                BNB USD     315.83     -11.43   -3.49%   49.867B  491.069M  157.889M
4           USD Coin USD   0.999511  -0.000294   -0.03%   33.768B    3.854B   33.785B
..                   ...        ...        ...      ...       ...       ...       ...
245        T-mac DAO USD     5.0286    +0.2064   +4.28%    5.029B   212,834        1B
246  Wrapped Bitcoin USD  26,954.66    -906.42   -3.25%     4.05B  127.609M   150,250
247        Chainlink USD     6.8675    -0.3538   -4.90%    3.551B  202.028M    517.1M
248     UNUS SED LEO USD     3.3762    -0.0793   -2.29%    3.221B    1.304M  953.954M
249           Cosmos USD      10.76      -0.57   -5.03%    3.082B   97.389M   286.37M

[250 rows x 7 columns]

'''

import requests 
from bs4 import BeautifulSoup 
import pandas as pd 

names=[]
prices=[]
changes=[]
percentChanges=[]
marketCaps=[]
totalVolumes=[]
circulatingSupplys=[]

for i in range(0,10):
 CryptoCurrenciesUrl = "https://finance.yahoo.com/crypto/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAGCyrqxf4eFC0Q82424qD8zS-43nOx2dmd1zSEd5x8EvjwHs-8xQImDBvaui6HnpnFGdA6YXbbjZOanBrmrrfRLEGITfNxwxu-WhaIkYpxufuI8pcy7XHe6qepL7TGMPAIOdGJlBAV8JF1NjY-SyQB4LwtMrf15XseAiJUy8ELDT"
 r = requests.get(CryptoCurrenciesUrl)
 data = r.text
 soup = BeautifulSoup(data, 'lxml')
 
 for listing in soup.find_all('tr', attrs={'class':'simpTblRow'}):
  for name in listing.find_all('td', attrs={'aria-label':'Name'}):
    names.append(name.text)
  for price in listing.find_all('td', attrs={'aria-label':'Price (Intraday)'}):
    prices.append(price.text)
  for change in listing.find_all('td', attrs={'aria-label':'Change'}):
    changes.append(change.text)
  for percentChange in listing.find_all('td', attrs={'aria-label':'% Change'}):
    percentChanges.append(percentChange.text)
  for marketCap in listing.find_all('td', attrs={'aria-label':'Market Cap'}):
    marketCaps.append(marketCap.text)
  for totalVolume in listing.find_all('td', attrs={'aria-label':'Volume in Currency (24Hr)'}):
    totalVolumes.append(totalVolume.text)
  for circulatingSupply in listing.find_all('td', attrs={'aria-label':'Circulating Supply'}):
     circulatingSupplys.append(circulatingSupply.text)


for i in range(0, 10):
 print(names[i], prices[i], changes[i], percentChanges[i], marketCaps[i], totalVolumes[i], circulatingSupplys[i])
'''
df=pd.DataFrame({"Names":names, "Prices":prices, "Changes":changes, "%Changes":percentChanges, "MarketCap":marketCaps, "Volume":totalVolumes, "Supplys":circulatingSupplys})
print(df)
'''

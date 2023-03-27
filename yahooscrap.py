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

df=pd.DataFrame({"Names":names, "Prices":prices, "Changes":changes, "%Changes":percentChanges, "MarketCap":marketCaps, "Volume":totalVolumes, "Supplys":circulatingSupplys})
print(df)

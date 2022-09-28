#importing prices which will be need to create the portfolio

import requests

url = 'http://api.nbp.pl/api/exchangerates/rates/c/usd/today/'
url2 = 'http://api.nbp.pl/api/exchangerates/rates/c/eur/today/'
url3 = 'http://api.nbp.pl/api/exchangerates/rates/c/gbp/today/'

response = requests.get(url)
responseEUR = requests.get(url2)
responseGBP = requests.get(url3)

tdata = response.json()
tdata2 = responseEUR.json()
tdata3 = responseGBP.json()

usd_todayBID = tdata["rates"][0]['bid'] #słownik - dictionary
eur_todayBID = tdata2["rates"][0]['bid']
gbp_todayBID = tdata3["rates"][0]['bid']

url = 'http://api.nbp.pl/api/exchangerates/rates/c/usd/2022-08-26/'
url2p = 'http://api.nbp.pl/api/exchangerates/rates/c/eur/2022-08-26'
url3p = 'http://api.nbp.pl/api/exchangerates/rates/c/gbp/2022-08-26'

responseUSDp = requests.get(url)
responseEURp = requests.get(url2p)
responseGBPp = requests.get(url3p)

data = responseUSDp.json()
pdata2 = responseEURp.json()
pdata3 = responseGBPp.json()

usd_pastask = data["rates"][0]['ask'] #słownik - dictionary
eur_pastask = pdata2["rates"][0]['ask']
gbp_pastask = pdata3["rates"][0]['ask']


#Data was downloaded, now it's time to create small portfolio to made of 3 currencies

#procentage = portfolio_(60,20,20) (usd,eur,gbp)

value_usd_wallet = round((0.6 * 1000 / usd_pastask),3)
value_eur_wallet = round((0.2 * 1000 / eur_pastask),3)
value_gbp_wallet = round((0.2 * 1000 / gbp_pastask),3)

print("Value of your wallet in USD after buy: " + str(value_usd_wallet))
print("Value of your wallet in EUR after buy: " + str(value_eur_wallet))
print("Value of your wallet in GBP after buy: " + str(value_gbp_wallet))

#Converting money back to PLN after 30 days of


value_pln_wallet1 = round((600 * usd_todayBID / usd_pastask),1)
value_pln_wallet2 = round((200 * eur_todayBID / eur_pastask),1)
value_pln_wallet3 = round((200 * usd_todayBID / gbp_pastask),1)

value_pln_wallet_final = (value_pln_wallet1 + value_pln_wallet2 + value_pln_wallet3)
print("Your estimated value of your wallet in PLN after 30 days is equal to: " + str(value_pln_wallet_final))

# Creating a plot of investment
import datetime as dt
import datetime
import matplotlib.pyplot as plt

url_chartusd = 'http://api.nbp.pl/api/exchangerates/rates/a/usd/last/30/'
url_charteur = 'http://api.nbp.pl/api/exchangerates/rates/a/eur/last/30/?format=csv'
url_chartgbp = 'http://api.nbp.pl/api/exchangerates/rates/a/gbp/last/30/?format=csv'

response_chartusd = requests.get(url_chartusd)
response_charteur = requests.get(url_charteur)
response_chartgbp = requests.get(url_chartgbp)

usdchartt = response_chartusd.json()
eurchartt = response_charteur.json()
gbpchartt = response_chartgbp.json()

#print(usdchartt)
#for 'effectiveDate', 'mid' in usdchartt.items[rates]():
    #print(str('effectiveDate')+str('mid'))

import pandas as pd

dfusd = pd.DataFrame(usdchartt)
#print(dfusd)









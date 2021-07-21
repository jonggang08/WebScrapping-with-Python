import requests
from bs4 import BeautifulSoup
import pandas as pd

mystocklist = ['AAPL', 'FB', 'AMC', 'PFE', 'GME']
stockdata = []

def getdata(symbol):
    url = f'https://finance.yahoo.com/quote/{symbol}'

    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    price = soup.find("span",{"class":"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
    change = soup.find("span", {"class":"Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)"}).text
    stock = { 'symbol' : symbol,
    'price' : price,
    'change' : change}
    return(stock)


    #price = soup.find("span",{"class":"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
    #change = soup.find("span", {"class":"Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)"}).text


for stock in mystocklist:
    stockdata.append(getdata(stock))
    #print('Getting: ', stock)



df = pd.DataFrame(stockdata)
df.to_excel("StockData.xlsx")
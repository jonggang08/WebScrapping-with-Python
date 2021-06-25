from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

url = "https://finance.yahoo.com/cryptocurrencies"

def extract(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    table = soup.find("table",{"class":"W(100%)"})
    coins = table.find_all("tr",{"class":"simpTblRow Bgc($hoverBgColor):h BdB Bdbc($seperatorColor) Bdbc($tableBorderBlue):h H(32px) Bgc($lv1BgColor)"})
    crypto=[]
    for coin in coins:
        name = coin.find("td",{"aria-label":"Name"}).text
        price = coin.find("td",{"aria-label":"Price (Intraday)"}).text
        change = coin.find("td",{"aria-label":"Change"}).text
        MarketCap = coin.find("td",{"aria-label":"Market Cap"}).text    
        Vol24 = coin.find("td",{"aria-label":"Volume in Currency (24Hr)"}).text
        Supply = coin.find("td",{"aria-label":"Circulating Supply"}).text        
        dict = {"Name":name, "Price":price, "Change": change, "MarketCap":MarketCap, "Volume24":Vol24, "Supply":Supply}
        crypto.append(dict)
    return crypto

data = extract(url)

df = pd.DataFrame(data)
df.to_csv("Crypto.csv")